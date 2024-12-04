import json

def save_contact(contacts):
    with open ('save_contact.json', 'w') as file:
        json.dump(contacts, file, indent=4)


def load_contact():
    with open('save_contact.json', 'r') as file:
        return json.load(file)