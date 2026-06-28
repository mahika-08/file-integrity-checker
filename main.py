from baseline import create_baseline
from integrity_checker import check_integrity

print("===== File Integrity Checker =====")
print("1. Create Baseline")
print("2. Check Integrity")

choice = input("Enter your choice: ")

if choice == "1":
    create_baseline()

elif choice == "2":
    check_integrity()

else:
    print("Invalid choice.")