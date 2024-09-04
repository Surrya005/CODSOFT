import json
import os

# Load contacts from a JSON file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to a JSON file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nContact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print("")

# Search for a contact
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip().lower()
    
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if not results:
        print("No matching contacts found.")
    else:
        for contact in results:
            print_contact_details(contact)

# Print detailed contact information
def print_contact_details(contact):
    print("\nContact Details:")
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}")
    print("")

# Update an existing contact
def update_contact(contacts):
    search_term = input("Enter name or phone number of the contact to update: ").strip().lower()
    
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            print_contact_details(contact)
            
            print("\nEnter new details (leave blank to keep current):")
            name = input(f"Name [{contact['name']}]: ").strip()
            phone = input(f"Phone [{contact['phone']}]: ").strip()
            email = input(f"Email [{contact['email']}]: ").strip()
            address = input(f"Address [{contact['address']}]: ").strip()
            
            if name:
                contact['name'] = name
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
            
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    
    print("No matching contacts found.")

# Delete a contact
def delete_contact(contacts):
    search_term = input("Enter name or phone number of the contact to delete: ").strip().lower()
    
    for i, contact in enumerate(contacts):
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            print_contact_details(contact)
            confirm = input("Are you sure you want to delete this contact? (y/n): ").strip().lower()
            if confirm == 'y':
                contacts.pop(i)
                save_contacts(contacts)
                print("Contact deleted successfully!")
                return
    
    print("No matching contacts found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
