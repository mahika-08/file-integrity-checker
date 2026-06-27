'''from hashing import generate_hash
file_hash = generate_hash("monitored/test.txt")
print(file_hash)
'''
'''
from scanner import scan_directory
files = scan_directory("monitored")
for file in files:
    print(file)
'''
from scanner import scan_directory
from hashing import generate_hash

files = scan_directory("monitored")

for file in files:

    file_hash = generate_hash(file)
    print(f"{file}")
    print(f"Hash: {file_hash}")
    print("-" * 60)