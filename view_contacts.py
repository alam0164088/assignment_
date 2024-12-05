def view_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
        return
    
    print("\nContact List:")

    for idx, contact in enumerate(contact_book, start=1):
        print(f"{idx}. Name: {contact['name']}, Email:{contact['email']} Phone: {contact['phone']} , Address: {contact['address']}")
        
        