# Log Archive & IP Intelligence Tool

This is a small Python script I wrote for practicing file handling and basic IP analysis.

### What it does
1. You give it a path to a log file.
2. It creates a new folder with a timestamp + random number.
3. It copies the log file into that folder.
4. It scans the archived log for IPv4 addresses.
5. It separates them into:
   - private IPs  
   - public IPs

### Why I made it
I wanted to learn how to:
- automate simple file archiving,
- extract IP addresses from logs,
- and use Python's `ipaddress` module.

### How to run it
