# Priv-Shield

A command-line tool that scans log files for sensitive data and masks it automatically. Built to help with KVKK and GDPR compliance — clean your logs before sharing them with third parties, uploading to cloud, or handing off to external teams.

## What It Detects

| Data Type       | Example                     | Masked As              |
|----------------|-----------------------------|------------------------|
| Email          | ahmet@company.com           | `<EMAIL_MASKED>`       |
| IP Address     | 192.168.1.14                | `<IP_MASKED>`          |
| National ID    | 30412876905                 | `<NATIONAL_ID_MASKED>` |
| Credit Card    | 4543-1234-5678-9010         | `<CC_MASKED>`          |
| Phone Number   | +90 532 444 12 89           | `<PHONE_MASKED>`       |

## Quick Start

No external dependencies — just Python 3.

```bash
git clone https://github.com/Emirzonee/Priv-Shield.git
cd Priv-Shield

python main.py sample.log
```

This reads `sample.log`, masks all sensitive data, and writes the result to `sample_masked.txt`.

## Example

**Before** (`sample.log`):
```
[2026-01-15 08:12:33] INFO  User login: ahmet.yilmaz@company.com from 192.168.1.14
[2026-01-15 08:15:44] INFO  Payment — CC: 4543-1234-5678-9010, user_id: 30412876905
```

**After** (`sample_masked.txt`):
```
[2026-01-15 08:12:33] INFO  User login: <EMAIL_MASKED> from <IP_MASKED>
[2026-01-15 08:15:44] INFO  Payment — CC: <CC_MASKED>, user_id: <NATIONAL_ID_MASKED>
```

**Report output:**
```
---------------------------------------------
  Input:    sample.log
  Output:   sample_masked.txt
  Size:     812 chars
---------------------------------------------
  email            4 match(es)
  ip_address       5 match(es)
  national_id      2 match(es)
  credit_card      2 match(es)
  phone            1 match(es)
---------------------------------------------
  Total masked: 14
---------------------------------------------
```

## How It Works

1. Takes a file path as a CLI argument
2. Reads the file content
3. Runs regex patterns for each sensitive data category
4. Replaces matches with placeholder tokens
5. Writes the cleaned output to a new file
6. Prints a summary report

All pattern matching is done with Python's built-in `re` module. Patterns are defined in a dictionary at the top of `main.py` so they're easy to extend — just add a new entry.

## Project Structure

```
Priv-Shield/
├── main.py          # Core script — detection and masking logic
├── sample.log       # Example log file for testing
├── .gitignore
├── LICENSE
└── README.md
```

## Limitations

- Regex-based detection can produce false positives (e.g. an 11-digit number that isn't a national ID)
- Only supports flat text files — no JSON/XML parsing yet
- No recursive directory scanning

## Possible Improvements

- Add JSON and CSV input support
- Configurable patterns via external YAML/JSON file
- Recursive mode for scanning entire directories
- Confidence scoring to reduce false positives

## License

MIT