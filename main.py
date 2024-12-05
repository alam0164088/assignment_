from file_loader import load_contacts_from_file
from save_file import save_contacts_to_file
from add_contact import add_contact
from view_contacts import view_contacts

from remove_contact import remove_contact
from search_contact import search_contact


def main():
    contact_book = load_contacts_from_file()

    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Save to File")
        print("6. Load From File")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            view_contacts(contact_book)
        elif choice == "3":
            remove_contact(contact_book)
        elif choice == "4":
            search_contact(contact_book)
        elif choice == "5":
            save_contacts_to_file(contact_book)
        elif choice == "6":
            contact_book = load_contacts_from_file()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


main()
