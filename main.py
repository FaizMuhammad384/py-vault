import os

# ==============================
# Python File Manager App (APPVAULT)
# ==============================


# Create File
def createFile(fileName):
    try:
        with open(fileName, "x") as file:
            print(f"{fileName} created successfully!")

    except FileExistsError:
        print(f"{fileName} already exists!")


# Read File
def readFile(fileName):
    try:
        with open(fileName, "r") as file:
            content = file.read()

            if content.strip() == "":
                print("File is empty!")
            else:
                print("\n===== FILE CONTENT =====")
                print(content)

    except FileNotFoundError:
        print(f"{fileName} not found!")

    except Exception as e:
        print(f"Error: {e}")


# Write File
def writeFile(fileName):
    try:
        text = input("Enter text to write: ")

        with open(fileName, "a") as file:
            file.write(text + "\n")

        print("Data written successfully!")

    except Exception as e:
        print(f"Error: {e}")


# Delete File
def deleteFile(fileName):
    try:
        os.remove(fileName)
        print(f"{fileName} deleted successfully!")

    except FileNotFoundError:
        print(f"{fileName} not found!")

    except Exception as e:
        print(f"Error: {e}")


# Main Function
# Main Function
def main():

    while True:

        print("\n========== APPVAULT FILE MANAGER ==========")
        print("1. Create File")
        print("2. Read File")
        print("3. Write File")
        print("4. Delete File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Exiting...")
            break

        fileName = input("Enter file name: ")

        if choice == "1":
            createFile(fileName)

        elif choice == "2":
            readFile(fileName)

        elif choice == "3":
            writeFile(fileName)

        elif choice == "4":
            deleteFile(fileName)

        else:
            print("Invalid Choice!")


# Run App
main()