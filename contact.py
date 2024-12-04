from create_contact import add_contact
from view_contact import view_contact
from remove_contact import remove_contact
from search_contact import search_contact



while True:
    print()
    print("Welcome To Contact Book Management ")
    print()
    print("0. Exit")
    print("1. Create a contact ")
    print("2. View contact")
    print("3. Remove contact")
    print("4. Search contact")

    choice = input("Enter Your Choice: ")

    if choice  == "0":
        print("Thanks For Using Contact Book Management System ")
        break

    elif choice == "1":
        name = input("Enter Contact Name: ")
        email = input("Enter Contact Email: ")
        number = int(input("Enter Contact Number: "))
        address = input("Enter Contact Address: ")
        add_contact(name,email,number,address)
        print("=====================")
        print("Contact Add Sucessfully ")
        print("=====================")
    elif choice == "2":
        view_contact()

    elif choice == "3":
        view_contact()
        index =int(input("Enter the index number to which contact do you want remove: "))
        remove_contact(index)
        print("Contact Number Delete Sucessfully")

    elif choice == "4":
        search = input("Search Contact Here: ")
        search_contact(search) 

    else:
        print("Invalid Choice")