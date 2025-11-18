# Log Archive & IP Intelligence Tool (Python)

This is a small Python script that does two things:

1. Creates a timestamped archive folder for a log file and copies the log file into it.
2. Reads the archived log file, finds IPv4 addresses, and separates them into private and public IPs.

I wrote it while practicing basic file handling and using the `ipaddress` module.

---

## Files

- `log_archive_ip_intel.py` – main script

---

## Requirements

- Python 3
- A text log file that may contain IPv4 addresses (for example, an app log or auth log).

---

## How to Run

From the terminal or command prompt:

```bash
python log_archive_ip_intel.py
