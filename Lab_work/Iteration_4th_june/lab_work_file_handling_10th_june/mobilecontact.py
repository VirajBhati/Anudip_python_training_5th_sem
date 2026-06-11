# Mobile Contact Directory System

FILE_NAME = "contacts.txt"


# ---------- Load contacts from file ----------
def load_contacts():
    contacts = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, number = line.strip().split(",")
                contacts[name] = number
    except FileNotFoundError:
        print("File not found. A new one will be created.")
    return contacts


# ---------- Save contacts to file ----------
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, number in contacts.items():
            file.write(f"{name},{number}\n")
    print("Changes saved successfully!")


# ---------- Display all contacts ----------
def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for name, number in contacts.items():
        print(f"{name} : {number}")


# ---------- Search contact ----------
def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found.")


# ---------- Add contact ----------
def add_contact(contacts):
    name = input("Enter name: ")
    number = input("Enter number: ")

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = number
        print("Contact added successfully.")


# ---------- Update contact ----------
def update_contact(contacts):
    name = input("Enter name to update: ")

    if name in contacts:
        new_number = input("Enter new number: ")
        contacts[name] = new_number
        print("Contact updated successfully.")
    else:
        print("Contact not found.")


# ---------- Delete contact ----------
def delete_contact(contacts):
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


# ---------- Names starting with vowel ----------
def vowel_contacts(contacts):
    vowels = "AEIOUaeiou"
    found = False

    print("\n--- Contacts Starting with Vowel ---")
    for name, number in contacts.items():
        if name[0] in vowels:
            print(f"{name} : {number}")
            found = True

    if not found:
        print("No contacts starting with a vowel.")


# ---------- Menu ----------
def menu():
    print("\n===== Mobile Contact Directory =====")
    print("1. Display all contacts")
    print("2. Search contact by name")
    print("3. Add new contact")
    print("4. Update contact number")
    print("5. Delete contact")
    print("6. Display names starting with vowel")
    print("7. Save changes")
    print("8. Exit")


# ---------- Main Program ----------
def main():
    contacts = load_contacts()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_contacts(contacts)

        elif choice == "2":
            search_contact(contacts)

        elif choice == "3":
            add_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            vowel_contacts(contacts)

        elif choice == "7":
            save_contacts(contacts)

        elif choice == "8":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


# Run program
main()