# contact-list

Shareable outreach contacts for Qimono projects: public institutional channels, researchers, universities, companies, quantum providers, government, and communities in Argentina and internationally. Started for the MIT xPRO essay on why "the time for investment is now".

## Files

| File | What it is | Use it for |
| --- | --- | --- |
| `qimono-contacts.vcf` | vCard 3.0, all contacts in one file | Apple Contacts, Google Contacts, Android, Outlook.com |
| `qimono-contacts.csv` | Google Contacts-style CSV | Google Contacts and CSV-compatible address books |
| `contacts.json` | Source of truth | Edit this one, then regenerate exports |

Every contact is tagged `Qimono - Quantum Outreach` plus a category. The list includes both confirmed quantum-technology contacts and general institutional leads that may route an inquiry to the relevant team.

## Updating

1. Edit `contacts.json`.
2. From the repository root, regenerate both exports:

   ```bash
   uv run qimono-contacts
   # or, without installing: PYTHONPATH=src python -m contact_list.build
   ```

3. Commit all three files together.

The builder lives in `src/contact_list/build.py` and uses only the Python standard library.

## Data quality rules

- Prefer public, official institutional contact details, contact forms, and professional profiles. Do not guess personal emails or phones.
- When a value cannot be verified, leave it empty and explain the gap in `note`.
- A company or institution listed for relevance is not necessarily known to be developing quantum technology. Distinguish an actual quantum program from a plausible use case or general outreach lead.
- Preserve a source URL in `web` and/or `note`.
- Verify role titles and contact details before outreach. Recheck time-sensitive facts before each campaign.
- `as_of` in `contacts.json` is the date the data was last checked.
