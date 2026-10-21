"""Build universal contact files from contact-list/contacts.json.

Outputs (written next to contacts.json):
  qimono-contacts.vcf  vCard 3.0, all contacts in one file (Apple Contacts, Google Contacts, Android, Outlook.com)
  qimono-contacts.csv  Google Contacts CSV format (Google Contacts, Outlook import)

contacts.json is the source of truth: edit it, then run from the repo root:
  uv run qimono-contacts            # or: python -m contact_list.build
  uv run qimono-contacts --dir path/to/other-list
"""
import argparse
import csv
import json
import sys
from pathlib import Path

DEFAULT_DIR = Path("contact-list")
SOCIAL_URL = {
    "x": "https://x.com/{}",
    "instagram": "https://www.instagram.com/{}",
    "tiktok": "https://www.tiktok.com/@{}",
}
APPLE_SERVICE = {"x": "Twitter", "instagram": "Instagram", "tiktok": "TikTok", "linkedin": "LinkedIn",
                 "facebook": "Facebook", "youtube": "YouTube", "discord": "Discord", "meetup": "Meetup"}


def social_links(social):
    """Return list of (label, url, handle_or_None)."""
    out = []
    for key, val in social.items():
        if key in SOCIAL_URL and not val.startswith("http"):
            out.append((key, SOCIAL_URL[key].format(val), val))
        else:
            out.append((key, val, None))
    return out


def esc(s):
    return (s or "").replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;").replace("\n", "\\n")


def fold(line):
    """RFC 2425 line folding at 75 octets."""
    data = line.encode("utf-8")
    if len(data) <= 75:
        return line
    parts, cur = [], b""
    for ch in line:
        b = ch.encode("utf-8")
        if len(cur) + len(b) > (75 if not parts else 74):
            parts.append(cur.decode("utf-8"))
            cur = b""
        cur += b
    parts.append(cur.decode("utf-8"))
    return "\r\n ".join(parts)


def vcard(c, list_name):
    person = c.get("person") or ""
    lines = ["BEGIN:VCARD", "VERSION:3.0"]
    if person:
        given, _, family = person.rpartition(" ")
        if not given:
            given, family = family, ""
        lines += [f"N:{esc(family)};{esc(given)};;;", f"FN:{esc(person)}"]
    else:
        lines += [f"N:;;;;", f"FN:{esc(c['org'])}", "X-ABShowAs:COMPANY"]
    lines.append(f"ORG:{esc(c['org'])}")
    if c.get("title"):
        lines.append(f"TITLE:{esc(c['title'])}")
    for e in c.get("emails", []):
        lines.append(f"EMAIL;TYPE=INTERNET,{e['type'].upper()}:{e['value']}")
    for p in c.get("phones", []):
        lines.append(f"TEL;TYPE={p['type'].upper()}:{p['value']}")
    a = c.get("address")
    if a:
        lines.append("ADR;TYPE=WORK:;;{};{};{};{};{}".format(
            esc(a.get("street")), esc(a.get("city")), esc(a.get("region")), esc(a.get("postal")), esc(a.get("country"))))
    n = 1
    if c.get("web"):
        lines += [f"item{n}.URL:{c['web']}", f"item{n}.X-ABLabel:website"]
        n += 1
    for key, url, handle in social_links(c.get("social", {})):
        lines += [f"item{n}.URL:{url}", f"item{n}.X-ABLabel:{APPLE_SERVICE.get(key, key)}"]
        n += 1
        user_param = f";x-user={handle}" if handle else ""
        lines.append(f"X-SOCIALPROFILE;TYPE={APPLE_SERVICE.get(key, key).lower()}{user_param}:{url}")
    lines.append(f"CATEGORIES:{esc(list_name)},{esc(c['category'])}")
    lines.append(f"NOTE:{esc(c.get('note', ''))}")
    lines.append(f"UID:qimono-{c['id']}")
    lines.append("END:VCARD")
    return "\r\n".join(fold(l) for l in lines) + "\r\n"


def google_csv_rows(contacts, list_name):
    max_e = max(len(c.get("emails", [])) for c in contacts) or 1
    max_p = max(len(c.get("phones", [])) for c in contacts) or 1
    max_w = max(1 + len(c.get("social", {})) for c in contacts)
    header = ["First Name", "Last Name", "Organization Name", "Organization Title", "Notes", "Labels"]
    for i in range(1, max_e + 1):
        header += [f"E-mail {i} - Label", f"E-mail {i} - Value"]
    for i in range(1, max_p + 1):
        header += [f"Phone {i} - Label", f"Phone {i} - Value"]
    header += ["Address 1 - Label", "Address 1 - Street", "Address 1 - City", "Address 1 - Region",
               "Address 1 - Postal Code", "Address 1 - Country"]
    for i in range(1, max_w + 1):
        header += [f"Website {i} - Label", f"Website {i} - Value"]
    rows = [header]
    for c in contacts:
        person = c.get("person") or ""
        given, _, family = person.rpartition(" ")
        if not given:
            given, family = family, ""
        row = [given, family, c["org"], c.get("title", ""), c.get("note", ""),
               f"{list_name} ::: {c['category']} ::: * myContacts"]
        emails = c.get("emails", [])
        for i in range(max_e):
            row += ["Work", emails[i]["value"]] if i < len(emails) else ["", ""]
        phones = c.get("phones", [])
        for i in range(max_p):
            row += ["Work", phones[i]["value"]] if i < len(phones) else ["", ""]
        a = c.get("address") or {}
        row += (["Work", a.get("street", ""), a.get("city", ""), a.get("region", ""), a.get("postal", ""),
                 a.get("country", "")] if a else [""] * 6)
        sites = ([("Website", c["web"])] if c.get("web") else []) + [
            (APPLE_SERVICE.get(k, k), url) for k, url, _ in social_links(c.get("social", {}))]
        for i in range(max_w):
            row += list(sites[i]) if i < len(sites) else ["", ""]
        rows.append(row)
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build .vcf and .csv contact files from contacts.json")
    parser.add_argument("--dir", type=Path, default=DEFAULT_DIR,
                        help="folder holding contacts.json; outputs are written there (default: contact-list)")
    args = parser.parse_args(argv)
    src = args.dir / "contacts.json"
    if not src.is_file():
        sys.exit(f"{src} not found (run from the repo root or pass --dir)")
    data = json.loads(src.read_text(encoding="utf-8"))
    contacts, list_name = data["contacts"], data["list_name"]
    ids = [c["id"] for c in contacts]
    if len(ids) != len(set(ids)):
        sys.exit("duplicate ids in contacts.json")
    (args.dir / "qimono-contacts.vcf").write_text("".join(vcard(c, list_name) for c in contacts),
                                                 encoding="utf-8", newline="")
    with open(args.dir / "qimono-contacts.csv", "w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerows(google_csv_rows(contacts, list_name))
    print(f"{len(contacts)} contacts written to {args.dir}")


if __name__ == "__main__":
    main()
