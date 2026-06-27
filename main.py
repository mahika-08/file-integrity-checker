from scanner import scan_directory
from hashing import generate_hash
from database import load_hashes, save_hashes

# Load previous hashes (baseline)
old_hashes = load_hashes()

# Dictionary for current scan
current_hashes = {}

# Scan all files
files = scan_directory("monitored")

for file in files:

    current_hash = generate_hash(file)
    current_hashes[file] = current_hash

    print(f"\nFile: {file}")
    print(f"Hash: {current_hash}")

    if file not in old_hashes:
        print("[NEW FILE]")

    elif old_hashes[file] != current_hash:
        print("[MODIFIED]")

    else:
        print("[UNCHANGED]")

    print("-" * 60)
# -----------------------------
# Compare old hashes with new
# -----------------------------

# Check for new or modified files
for file, current_hash in current_hashes.items():

    if file not in old_hashes:
        print(f"[NEW FILE] {file}")

    elif old_hashes[file] != current_hash:
        print(f"[MODIFIED] {file}")

    else:
        print(f"[UNCHANGED] {file}")

# Check for deleted files
for file in old_hashes:

    if file not in current_hashes:
        print(f"[DELETED] {file}")

# Save current hashes as the new baseline
save_hashes(current_hashes)