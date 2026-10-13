files = []

def create_file():
    name = input("Enter file name: ").strip()

    if not name:
        print("File name cannot be empty!")
    elif name in files:
        print("File already exists!")
    else:
        files.append(name)
        print("File created successfully!")

def search_file():
    name = input("Enter file name to search: ").strip()

    if name in files:
        print("File found successfully!")
    else:
        print("File not found!")

def display_files():
    print("\n--- Directory Contents ---")

    if len(files) == 0:
        print("Directory is empty.")
    else:
        for i, name in enumerate(files, start=1):
            print(f"{i}. {name}")

    print("Total files:", len(files))

while True:
    print("\n=== FILE DIRECTORY SIMULATOR ===")
    print("1. Create File")
    print("2. Search File")
    print("3. Display Files")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        create_file()
    elif choice == "2":
        search_file()
    elif choice == "3":
        display_files()
    elif choice == "4":
        print("Module 1 completed successfully!")
        break
    else:
        print("Invalid choice! Enter 1, 2, 3, or 4.")
