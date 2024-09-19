import json

def read_contacts_from_json(filename='contacts.json'):
    """Read the contacts from a JSON file"""
    with open(filename, 'r') as f:
        contacts = json.load(f)
    return contacts

def print_contacts(contacts):
    """Print contact names and phone numbers in two columns"""
    print(f"{'Name':<30} {'Phone Number':<15}")
    print('-' * 45)
    
    for person in contacts:
        name = person.get('names', [{'displayName': 'No Name'}])[0]['displayName']
        phone_numbers = person.get('phoneNumbers', [{'value': 'No Number'}])
        # Print all phone numbers for the person
        for phone in phone_numbers:
            phone_number = phone['value']
            print(f"{name:<30} {phone_number:<15}")

def main():
    contacts = read_contacts_from_json()
    print_contacts(contacts)

if __name__ == '__main__':
    main()
