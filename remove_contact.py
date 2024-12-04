from save_contact import load_contact,save_contact

def remove_contact(index):
    contacts = load_contact()
    if 0< index <=len(contacts):
        del contacts[index-1]
        save_contact(contacts)
    else:
        print("invalid index")    