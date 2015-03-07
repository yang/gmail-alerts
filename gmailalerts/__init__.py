__author__ = 'yang'

import sys
import httplib2
import path

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'



def create_service(secrets_path, cred_storage):
  # Start the OAuth flow to retrieve credentials
  flow = flow_from_clientsecrets(secrets_path, scope=OAUTH_SCOPE)
  http = httplib2.Http()
  # Try to retrieve credentials from storage or run the flow to generate them
  credentials = cred_storage.get()
  if credentials is None or credentials.invalid:
    credentials = run(flow, cred_storage, http=http)

  # Authorize the httplib2.Http object with our credentials
  http = credentials.authorize(http)
  # Build the Gmail service from discovery
  gmail_service = build('gmail', 'v1', http=http)
  return gmail_service


def main(argv=sys.argv):
  basedir = path.Path('~/.gmail-alerts/').expanduser()
  # Path to the client_secret.json file downloaded from the Developer Console
  secrets_path = basedir / 'client_secret.json'
  # Location of the credentials storage file
  cred_storage = Storage(basedir / 'cred_store.json')

  gmail_service = create_service(secrets_path, cred_storage)

  # Retrieve a page of threads
  threads = gmail_service.users().threads().list(userId='me').execute()

  # Print ID for each thread
  if threads['threads']:
    for thread in threads['threads']:
      print 'Thread ID: %s' % (thread['id'])
