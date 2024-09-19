import json

# Your UPI ID (static, since you are requesting the payment)
MY_UPI_ID = "jaysanhelix@okaxis"

# Function to load contacts from the contacts.json file
def load_contacts(file_path="contacts.json"):
    with open(file_path, 'r') as file:
        contacts = json.load(file)
    return contacts

# Function to search for a contact by name
def find_contact_by_name(contacts, name):
    for contact in contacts:
        if 'names' in contact and contact['names'][0]['displayName'].lower() == name.lower():
            return contact
    return None

# Function to generate UPI payment link
def generate_upi_link(upi_id, name, amount, currency="INR"):
    # Remove spaces from the name
    name_no_spaces = name.replace(" ", "")
    upi_link = f"upi://pay?pa={upi_id}&pn={name_no_spaces}&am={amount}&cu={currency}"
    return upi_link

def main():
    # Load contacts from the json file
    contacts = load_contacts()

    # Ask user for the contact name
    contact_name = input("Enter the name of the contact: ")

    # Find the contact in the contacts.json file
    contact = find_contact_by_name(contacts, contact_name)

    if contact:
        contact_name = contact['names'][0]['displayName']
        phone_number = contact['phoneNumbers'][0]['canonicalForm']
        print(f"Contact found: {contact_name} (Phone: {phone_number})")

        # Ask the user for the amount to request
        amount = input(f"Enter the amount to request from {contact_name}: ")

        # Generate the UPI payment link (using your UPI ID)
        upi_link = generate_upi_link(MY_UPI_ID, contact_name, amount)
        print(f"Generated UPI Payment Link: {upi_link}")
        
        # You can extend this code to send the link via SMS or other methods
        print(f"Share this link with {contact_name}: {upi_link}")

    else:
        print("Contact not found.")

if __name__ == "__main__":
    main()
