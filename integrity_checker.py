from scanner import scan_directory
from hashing import generate_hash
from database import load_hashes
from logger import log_change

def check_integrity():

    old_hashes = load_hashes()

    current_hashes = {}

    files = scan_directory("monitored")

    for file in files:
        current_hashes[file] = generate_hash(file)

    for file, current_hash in current_hashes.items():

        if file not in old_hashes:
            print(f"[NEW FILE] {file}")
            log_change("NEW FILE", file)

        elif old_hashes[file] != current_hash:
            print(f"[MODIFIED] {file}")
            log_change("MODIFIED", file)

        else:
            print(f"[UNCHANGED] {file}")

    for file in old_hashes:

        if file not in current_hashes:
            print(f"[DELETED] {file}")
            log_change("DELETED", file)