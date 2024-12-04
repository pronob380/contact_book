from save_contact import save_contact,load_contact
 

def add_contact(name, email, number,address):
    contacts = load_contact()
    contact = {
        'name': name,
        'email': email,
        'number': number,
        'address': address
    }
    contacts.append(contact)
    save_contact(contacts)