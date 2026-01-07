"""
Priv-Shield — Data Anonymization Tool

Scans log files for sensitive information (emails, IPs, credit cards,
national IDs) and replaces them with masked placeholders.
Useful for KVKK/GDPR compliance before sharing data externally.
"""

import re
import sys
import os
from datetime import datetime


# regex patterns for each sensitive data type
PATTERNS = {
    "email":       (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', "<EMAIL_MASKED>"),
    "ip_address":  (r'\b(?:\d{1,3}\.){3}\d{1,3}\b', "<IP_MASKED>"),
    "national_id": (r'\b\d{11}\b', "<NATIONAL_ID_MASKED>"),
    "credit_card": (r'\b(?:4\d{3}|5[0-5]\d{2})[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b', "<CC_MASKED>"),
    "phone":       (r'(?:\+90|0)\s?\d{3}\s?\d{3}\s?\d{2}\s?\d{2}', "<PHONE_MASKED>"),
}


def load_file(path):
    """Read file content, return as string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def mask_sensitive_data(text):
    """
    Run all regex patterns against the text.
    Returns the masked text and a dict with match counts per category.
    """
    stats = {}
    masked = text

    for label, (pattern, placeholder) in PATTERNS.items():
        found = re.findall(pattern, masked)
        if found:
            masked = re.sub(pattern, placeholder, masked)
            stats[label] = len(found)

    return masked, stats


def write_output(content, output_path):
    """Write masked content to a new file."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def print_report(input_path, output_path, stats, original_size):
    """Print a summary of what was masked."""
    total = sum(stats.values())

    print("-" * 45)
    print(f"  Input:    {input_path}")
    print(f"  Output:   {output_path}")
    print(f"  Size:     {original_size} chars")
    print("-" * 45)

    if total == 0:
        print("  No sensitive data found.")
    else:
        for label, count in stats.items():
            print(f"  {label:<15} {count} match(es)")
        print("-" * 45)
        print(f"  Total masked: {total}")

    print("-" * 45)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <logfile>")
        print("Example: python main.py sample.log")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.isfile(input_path):
        print(f"[!] File not found: {input_path}")
        sys.exit(1)

    # build output filename: sample.log -> sample_masked.txt
    base, _ = os.path.splitext(input_path)
    output_path = f"{base}_masked.txt"

    print(f"\n[*] Priv-Shield starting...")
    print(f"[*] Scanning: {input_path}\n")

    content = load_file(input_path)
    masked, stats = mask_sensitive_data(content)
    write_output(masked, output_path)

    print_report(input_path, output_path, stats, len(content))
    print(f"\n[+] Done. Masked file saved to: {output_path}")


if __name__ == "__main__":
    main()