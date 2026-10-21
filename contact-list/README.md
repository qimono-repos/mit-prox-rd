# contact-list

Shareable outreach contacts for Qimono (TM) projects: government offices, universities, companies and communities related to quantum computing in Argentina and abroad. Started for the MIT xPRO essay on why "the time for investment is now".

## Files

| File | What it is | Use it for |
| --- | --- | --- |
| `qimono-contacts.vcf` | vCard 3.0, all contacts in one file | Apple Contacts, Google Contacts, Android. Open the file or import it. |
| `qimono-contacts.csv` | Google Contacts CSV | Google Contacts and Outlook (Outlook desktop only imports the first contact of a multi-contact .vcf) |
| `contacts.json` | Source of truth | Edit this one, never the .vcf or .csv by hand |

Every contact is tagged `Qimono - Quantum Outreach` plus a category (Government - National, Academia - Quantum, Company - Fintech, ...), so they import as a group.

## Updating

1. Edit `contacts.json`.
2. From the repo root, regenerate both files:

   ```bash
   uv run qimono-contacts
   # or, without installing: PYTHONPATH=src python -m contact_list.build
   ```

3. Commit all three files together.

The builder lives in `src/contact_list/build.py`. It only uses the Python standard library.

## Data rules

- Only public, official contact details (institutional sites, press releases). No personal emails or phones.
- When a value could not be verified, it stays empty and the `note` says what is missing.
- `as_of` in `contacts.json` is the date the data was last checked.
