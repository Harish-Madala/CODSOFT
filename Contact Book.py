def display_menu():
    print("\n=== Contact Book Menu ===")
    print("1. View Contact List")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts available.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully.")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip().lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            index = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= index < len(contacts):
                contacts[index]['name'] = input("Enter new name: ").strip() or contacts[index]['name']
                contacts[index]['phone'] = input("Enter new phone number: ").strip() or contacts[index]['phone']
                contacts[index]['email'] = input("Enter new email: ").strip() or contacts[index]['email']
                contacts[index]['address'] = input("Enter new address: ").strip() or contacts[index]['address']
                print("Contact updated successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= index < len(contacts):
                contacts.pop(index)
                print("Contact deleted successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    contacts = []
    print("=== Welcome to the Contact Book ===")

    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                view_contacts(contacts)
            elif choice == 2:
                add_contact(contacts)
            elif choice == 3:
                search_contact(contacts)
            elif choice == 4:
                update_contact(contacts)
            elif choice == 5:
                delete_contact(contacts)
            elif choice == 6:
                print("Exiting the Contact Book.")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
