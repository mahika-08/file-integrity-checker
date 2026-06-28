from scanner import scan_directory
from hashing import generate_hash
from database import save_hashes

def create_baseline():

    files = scan_directory("monitored")

    hashes = {}

    for file in files:

        hashes[file] = generate_hash(file)

    save_hashes(hashes)

    print("Baseline created successfully.")