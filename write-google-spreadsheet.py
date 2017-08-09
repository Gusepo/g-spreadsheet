
# coding: utf-8

# In[1]:

import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import gspread
import requests 
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = creds = ServiceAccountCredentials.from_json_keyfile_name('json_keyfile_name.json', scope) #go to https://console.developers.google.com/ to get your credentials - check http://bit.ly/2lqV4ao for a step by step tutorial 
http = credentials.authorize(httplib2.Http())

client = gspread.authorize(creds)

discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)


spreadsheet_id = 'spreadsheet_id' #Get spreadsheet ID from spreadsheet URL
range_name = 'Foglio1!A1:C3' #name of the sheet and cells interval
value_input_option = 'USER_ENTERED' #convert types as they were inserted from GUI


# In[41]:

values = [
    ["value A1", "value B1", "value C1"],
    ["value A2", "value B2", "value C2"],
    ["value A3", "value B3", "value C3"],
    ];
body = {
  'values': values
}
result = service.spreadsheets().values().update(
    spreadsheetId=sheet_id, range=range_name,
    valueInputOption=value_input_option, body=body).execute()


# In[ ]:



