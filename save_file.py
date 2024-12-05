import csv

def save_contacts_to_file(contact_book, filename="contacts.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name","email", "phone", "address"])
        writer.writeheader()
        writer.writerows(contact_book)
    print("Contacts saved to file successfully!")
