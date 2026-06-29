from scanner import scan_directory
from hashing import generate_hash
from database import load_hashes
from logger import log_change

def check_integrity(folder):
    """
    Returns a dict:
    {
      "stats": {"scanned": N, "modified": N, "new": N, "deleted": N, "unchanged": N},
      "files": [{"name": "...", "status": "UNCHANGED|MODIFIED|NEW|DELETED"}, ...]
    }
    """
    old_hashes = load_hashes()
    current_hashes = {}

    files = scan_directory(folder)
    for file in files:
        current_hashes[file] = generate_hash(file)

    file_results = []

    for file, current_hash in current_hashes.items():
        if file not in old_hashes:
            file_results.append({"name": file, "status": "NEW"})
            log_change("NEW FILE", file)
        elif old_hashes[file] != current_hash:
            file_results.append({"name": file, "status": "MODIFIED"})
            log_change("MODIFIED", file)
        else:
            file_results.append({"name": file, "status": "UNCHANGED"})

    for file in old_hashes:
        if file not in current_hashes:
            file_results.append({"name": file, "status": "DELETED"})
            log_change("DELETED", file)

    stats = {
        "scanned": len(file_results),
        "unchanged": sum(1 for r in file_results if r["status"] == "UNCHANGED"),
        "modified":  sum(1 for r in file_results if r["status"] == "MODIFIED"),
        "new":       sum(1 for r in file_results if r["status"] == "NEW"),
        "deleted":   sum(1 for r in file_results if r["status"] == "DELETED"),
    }

    return {"stats": stats, "files": file_results}