from save_contact import load_contact

def search_contact(search):
    contacts = load_contact
    result = []
    for contact in contacts:  
        if search.lower() in contact['name'].lower() or search in contact['email'].lower()  or search in contact['number'] or search in contact['address'].lower():
            result.append(contact)
        else:
            print("Invalid Search")    
    print("Search Results: ")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}, Address: {contact['address']}")
