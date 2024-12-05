import csv

def load_contacts_from_file(filename="contacts.csv"):
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print("No saved contacts found. Starting with an empty contact book.")
        return []
