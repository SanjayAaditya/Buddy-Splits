import os
import json
import pickle
import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']

def authenticate_google():
    """Authenticate the user and return the service object for Google People API"""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('people', 'v1', credentials=creds)
    return service

def get_contacts(service):
    """Get a list of contacts from the Google People API"""
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1000,
        personFields='names,emailAddresses,phoneNumbers'
    ).execute()

    connections = results.get('connections', [])
    return connections

def save_contacts_to_json(contacts, filename='contacts.json'):
    """Save the contacts to a JSON file"""
    with open(filename, 'w') as f:
        json.dump(contacts, f, indent=4)
    print(f'Contacts saved to {filename}')

def main():
    service = authenticate_google()
    contacts = get_contacts(service)
    save_contacts_to_json(contacts)

if __name__ == '__main__':
    main()
