

def is_duplicate(contact_book, phone):
   
    for contact in contact_book:
        if contact["phone"] == phone:
            print(f"The phone number {phone} is already assigned to {contact['name']}.")
            return True  
    return False  
