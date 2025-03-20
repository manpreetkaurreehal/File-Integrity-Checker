# File-Integrity-Checker

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MANPREET KAUR

*INTERN ID*: CT6WUNN

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

**OVERVIEW**

A Python-based tool to monitor and verify file integrity by calculating and comparing hash values.

This script provides an easy yet efficient way of checking file integrity in a specified directory. Using the SHA-256 hash function, it creates a starting point for file hashes and allows you to detect changes, additions, or deletions over time. Ideal for system administrators, developers, or anyone who needs to check for file consistency.

A file integrity checker is a tool or software used to scan and confirm the integrity of files in a system for detecting changes, modifications, or corruption. It guarantees that files do not change from their original or expected form, and this is required for security, data integrity, and system integrity.

**Features**

1.Class Structure: Uses a FileIntegrityChecker class to organize the functionality.

2.Hash Calculation:

-Uses SHA-256 (via hashlib) for secure file hashing

-Reads files in chunks to handle large files efficiently

-Returns hexadecimal hash values

3.Baseline Creation:

-Scans specified directory recursively

-Stores file hashes, modification times, and sizes in a JSON file

-Uses relative paths for consistency

4.Integrity Checking:

-Compares current file states against baseline

-Detects new, modified, and deleted files

-Provides detailed change reports

5.User Interface:

-Simple menu-driven interface

-Option to create baseline or check integrity

-Clear output formatting

**How It Works?**

Baseline Creation: Scans a directory (e.g., C:\Users\Manpreet\Documents). Computes SHA-256 hashes for each file. Saves hashes and metadata (size, modification time) in file_hashes.json.

Monitoring Changes: Rescans and compares current hashes to the baseline.

Reporting: Flags new, modified, or deleted files (e.g., "MODIFIED FILE: report.txt").

**Core Mechanism: Hashing**

What’s a Hash?: A cryptographic function (e.g., SHA-256) generates a fixed-length string from file contents.
Example: "Hello" might hash to a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e.Change to "Hello!" and the hash becomes entirely different.

Why It’s Reliable: Even tiny changes produce a new hash, ensuring accurate detection.

**Tools Used**

Python 3: Core programming language (version 3.6+ recommended).

hashlib: Built-in library for SHA-256 hashing, ensuring secure fingerprints.

os: Library for directory traversal (os.walk) and file metadata (getmtime, getsize).

json: Library to store baseline data in file_hashes.json.

PyCharm: IDE for writing, debugging, and running the script.

**Example Outputs**

Scenario 1: Creating a Baseline

![Image](https://github.com/user-attachments/assets/698f9de2-c99b-49e1-b6ad-8d40080513e4)

(The script creates a file_hashes.json file containing hashes of all files in E:\PROJECTS\cpp projects)

Scenario 2: First Integrity Check (No Changes)

![Image](https://github.com/user-attachments/assets/8d64bcfd-f327-47cb-a2ed-782c35a845b5)

(no files were changed since the baseline was created)

Scenario 3: Integrity Check (Modified File)

![Image](https://github.com/user-attachments/assets/76ed606f-fcd3-446c-869d-4609f96edd8d)

(atm.cpp was modified)

Scenario 4: Integrity Check (New and Deleted Files)

Scenario 5: Error Cases

a) Directory Doesn't Exist

b) No Baseline Exists

