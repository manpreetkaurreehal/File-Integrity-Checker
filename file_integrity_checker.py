import hashlib
import os
import json
import time
from datetime import datetime


class FileIntegrityChecker:
    def __init__(self, directory_path):
        """Initialize the integrity checker with a directory to monitor."""
        self.directory_path = directory_path
        self.baseline_file = "file_hashes.json"
        self.hash_algorithm = hashlib.sha256  # Using SHA-256 for secure hashing

    def calculate_file_hash(self, file_path):
        """Calculate the hash of a file."""
        hasher = self.hash_algorithm()
        try:
            with open(file_path, "rb") as f:
                # Read file in chunks to handle large files efficiently
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except (IOError, OSError) as e:
            print(f"Error reading {file_path}: {e}")
            return None

    def create_baseline(self):
        """Create a baseline of file hashes for all files in directory."""
        file_hashes = {}

        if not os.path.exists(self.directory_path):
            print(f"Directory {self.directory_path} does not exist!")
            return False

        for root, _, files in os.walk(self.directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_hash = self.calculate_file_hash(file_path)
                if file_hash:
                    # Store relative path as key to maintain consistency
                    relative_path = os.path.relpath(file_path, self.directory_path)
                    file_hashes[relative_path] = {
                        "hash": file_hash,
                        "last_modified": os.path.getmtime(file_path),
                        "size": os.path.getsize(file_path)
                    }

        # Save baseline to JSON file
        try:
            with open(self.baseline_file, "w") as f:
                json.dump(file_hashes, f, indent=4)
            print(f"Baseline created successfully: {self.baseline_file}")
            return True
        except Exception as e:
            print(f"Error saving baseline: {e}")
            return False

    def check_integrity(self):
        """Check current files against baseline and report changes."""
        if not os.path.exists(self.baseline_file):
            print("Baseline file not found! Please create a baseline first.")
            return

        # Load baseline hashes
        try:
            with open(self.baseline_file, "r") as f:
                baseline_hashes = json.load(f)
        except Exception as e:
            print(f"Error loading baseline: {e}")
            return

        current_hashes = {}
        changes_detected = False

        # Calculate current hashes
        for root, _, files in os.walk(self.directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(file_path, self.directory_path)
                current_hash = self.calculate_file_hash(file_path)
                if current_hash:
                    current_hashes[relative_path] = {
                        "hash": current_hash,
                        "last_modified": os.path.getmtime(file_path),
                        "size": os.path.getsize(file_path)
                    }

        # Compare with baseline
        print("\nFile Integrity Check Results:")
        print("============================")

        # Check for modified or new files
        for file_path, current_data in current_hashes.items():
            if file_path not in baseline_hashes:
                print(f"NEW FILE DETECTED: {file_path}")
                changes_detected = True
            elif current_data["hash"] != baseline_hashes[file_path]["hash"]:
                print(f"MODIFIED FILE: {file_path}")
                print(f"Old hash: {baseline_hashes[file_path]['hash']}")
                print(f"New hash: {current_data['hash']}")
                changes_detected = True

        # Check for deleted files
        for file_path in baseline_hashes:
            if file_path not in current_hashes:
                print(f"DELETED FILE: {file_path}")
                changes_detected = True

        if not changes_detected:
            print("No changes detected. All files match the baseline.")


def main():
    # Example usage
    directory_to_monitor = input("Enter the directory path to monitor: ")
    checker = FileIntegrityChecker(directory_to_monitor)

    while True:
        print("\nFile Integrity Checker Menu:")
        print("1. Create baseline")
        print("2. Check integrity")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            checker.create_baseline()
        elif choice == "2":
            checker.check_integrity()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()