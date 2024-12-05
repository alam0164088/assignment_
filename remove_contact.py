

def remove_contact(contact_book):
    phone = input("Enter the phone number of the contact to remove: ")
    
    for contact in contact_book:
        if contact["phone"] == phone:
            contact_book.remove(contact)
            print(f"Contact with phone number {phone} removed successfully!")
            return
    
    print(f"No contact found with the phone number {phone}.")