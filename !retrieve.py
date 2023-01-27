#This is a modified version of Google's Docs API Python Quickstart code.
#I hope to understand how this API works enough to simplify this code to do only what I need, but for now it has a lot of extra code left over from the template.

'''
also I just realized this code has a workaround for multi-line comments in 
Python 
!
:)
'''

"""
Recursively extracts the text from a Google Doc.
"""
import googleapiclient.discovery as discovery
from httplib2 import Http
from oauth2client import client
from oauth2client import file
from oauth2client import tools
import os
import json
import re



SCOPES = 'https://www.googleapis.com/auth/documents.readonly'
DISCOVERY_DOC = 'https://docs.googleapis.com/$discovery/rest?version=v1'
DOCUMENT_ID = '1MWA0YQjvkMV7MiMHet_eddj7cXRPnKXVpO3Nc0Wckx4'

#the comments surrounded by """ are from the original Google code. 
def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth 2.0 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    store = file.Storage('token.json')
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        credentials = tools.run_flow(flow, store)
    return credentials

def read_paragraph_element(element):
    """Returns the text in the given ParagraphElement.

        Args:
            element: a ParagraphElement from a Google Doc.
    """
    text_run = element.get('textRun')
    if not text_run:
        return ''
    return text_run.get('content')


def read_structural_elements(elements):
    """Recurses through a list of Structural Elements to read a document's text where text may be
        in nested elements.

        Args:
            elements: a list of Structural Elements.
    """
    #Here's where my modification starts. First, I made 2 empty vars. One string and one list. 
    text = ''
    lst = []
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(elem)
        elif 'table' in value:
            # The text in table cells are in nested Structural Elements and tables may be
            # nested.
            table = value.get('table')
            for row in table.get('tableRows'):
                cells = row.get('tableCells')
                for cell in cells:
                    text += read_structural_elements(cell.get('content'))
                    #I needed each cell turned into a string, so I tested with print() until I found that this code outputs strings. 
                    #I appended these to the python list.
                    lst.append(read_structural_elements(cell.get('content')))
                    #Opened the JSON file I made.
                    with open("psychsyllabus.json", "r") as f:
                        #I'm pretty sure the below line does nothing, but in an effort to make sure the code doesn't break I am leaving it until my next version. 
                        data = json.load(f)
                        #Sets the data var to the Python list of cells turned into strings.
                        data = lst
                    #Opens the JSON in write mode so it can dump the list to the JSON file. 
                    with open('psychsyllabus.json', 'w') as f:
                        json.dump(data, f, indent=2)
        elif 'tableOfContents' in value:
            # The text in the TOC is also in a Structural Element.
            toc = value.get('tableOfContents')
            text += read_structural_elements(toc.get('content'))
    return text



def main():
    """Uses the Docs API to print out the text of a document."""
    credentials = get_credentials()
    print(credentials)
    http = credentials.authorize(Http())
    docs_service = discovery.build(
        'docs', 'v1', http=http, discoveryServiceUrl=DISCOVERY_DOC)
    doc = docs_service.documents().get(documentId=DOCUMENT_ID).execute()
    doc_content = doc.get('body').get('content')
    
    doc_json = read_structural_elements(doc_content)
 
        
    

if __name__ == '__main__':
    main()

with open("psychsyllabus.json", "r") as f:
    data = json.load(f)

print(data)