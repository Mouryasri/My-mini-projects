import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone =input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(contacts):
    query = input("Enter name or phone number to search: ").strip().lower()
    results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]
    
    if not results:
        print("No contacts found.")
        return
    
    print("\nSearch Results:")
    for contact in results:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact(contacts):
    query = input("Enter name or phone number to update: ").strip().lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            contact['name'] = input("Enter new name (leave blank to keep current): ").strip() or contact['name']
            contact['phone'] = input("Enter new phone number (leave blank to keep current): ").strip() or contact['phone']
            contact['email'] = input("Enter new email (leave blank to keep current): ").strip() or contact['email']
            contact['address'] = input("Enter new address (leave blank to keep current): ").strip() or contact['address']
            save_contacts(contacts)
            print("Contact updated successfully.")
            return

    print("No contact found with the given name or phone number.")

def delete_contact(contacts):
    query = input("Enter name or phone number to delete: ").strip().lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return

    print("No contact found with the given name or phone number.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
