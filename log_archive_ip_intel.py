# log_archive_ip_intel.py

import os
import time
import random
import shutil
import ipaddress

def archive_log_file(log_filename):
    # checks if the file exists
    if not os.path.isfile(log_filename):
        print(f"File '{log_filename}' was not found.")
        return None

    # creates a unique directory name based on date and a random number
    timestamp = time.strftime("%m%d%Y_%H%M%S")
    rand_num = random.randint(100, 999)
    base_name = os.path.splitext(os.path.basename(log_filename))[0]
    archive_dir_name = f"{timestamp}_{base_name}_archive_{rand_num}"

    # builds the full path for the new folder
    archive_dir = os.path.join(os.path.dirname(log_filename), archive_dir_name)

    # actually creates the directory
    os.makedirs(archive_dir, exist_ok=True)

    # copies the file into the new folder
    archived_path = os.path.join(archive_dir, os.path.basename(log_filename))
    shutil.copy2(log_filename, archived_path)

    print(f"Copied '{log_filename}' into '{archived_path}'")
    return archived_path


def analyze_log_ips(log_path):
    # here we will keep unique private and public IPs
    private_ips = set()
    public_ips = set()

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            words = line.split()
            for word in words:
                try:
                    ip = ipaddress.ip_address(word)
                    # we only care about IPv4 here
                    if ip.version == 4:
                        if ip.is_private:
                            private_ips.add(str(ip))
                        elif ip.is_global:
                            public_ips.add(str(ip))
                except ValueError:
                    # not an IP, just skip
                    continue

    return private_ips, public_ips


def main():
    log_name = input("Enter the path to a log file:\n").strip()
    if not log_name:
        print("No file given, exiting.")
        return

    archived = archive_log_file(log_name)
    if not archived:
        return

    private_ips, public_ips = analyze_log_ips(archived)

    print("\n--- IP Analysis Report ---")
    print(f"Private IPv4 addresses ({len(private_ips)}):")
    for ip in sorted(private_ips):
        print(" ", ip)

    print(f"\nPublic IPv4 addresses ({len(public_ips)}):")
    for ip in sorted(public_ips):
        print(" ", ip)


if __name__ == "__main__":
    main()
