

def search_contact(contact_book):
    phone = input("Enter the phone number of the contact to search: ")
    
    for contact in contact_book:
        if contact["phone"] == phone:
          
            print(f"Contact found: Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
            return
    
    print(f"No contact found with the phone number {phone}.")
