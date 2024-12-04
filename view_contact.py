from save_contact import load_contact

def view_contact():
    contacts = load_contact()
    print("===================")
    print("  Contact List")
    print("===================")
    for i, contact in enumerate(contacts):
        if isinstance(contact, dict):
            print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}, Address: {contact['address']}")


