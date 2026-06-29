from scanner import scan_directory
from hashing import generate_hash
from database import save_hashes

def create_baseline(folder):

    files = scan_directory(folder)

    hashes = {}

    for file in files:

        hashes[file] = generate_hash(file)

    save_hashes(hashes)

    return "✅ Baseline created successfully."