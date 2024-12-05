# add_contact.py

from prevent_duplicate import is_duplicate

def add_contact(contact_book):
    name = input("Enter contact name: ")
    email=input("Enter Email: ")
    phone = int(input("Enter phone number: "))
    address=input("Enter address number: ")
    
   
    if is_duplicate(contact_book, phone):
        print("This phone number already exists!")
        return
    
    contact_book.append({"name": name,"email":email ,"phone": phone, "address":address,})
    print("Contact added successfully!")
