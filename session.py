import requests
import json
import base64
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

BASE_URL = 'https://goclick.atlassian.net'
email = os.getenv('EMAIL')
token = os.getenv('TOKEN')
credentials = f"{email}:{token}"
# print(credentials.encode("utf-8"))


def get_session():
   cred =  "Basic " + base64.b64encode(credentials.encode("utf-8")).decode("utf-8") 
      # print(cred)
   headers = {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization" : cred
   }

   jql = f'assignee = currentUser()'

   url = f"{BASE_URL}/rest/api/3/search?jql=assignee=" + 'currentUser()'

   # Send request and get response
   response = requests.request(
      "GET", 
      url,
      headers=headers
   )

   return response

# get_session()
# print(get_session())
# reponse = get_session()
# print(reponse.status_code)

# json_data = json.loads(get_session().text)

# print(json_data['issues'][0]['fields'])

# for issue in json_data['issues']:
#    jira_number = issue['key']
#    description = issue['fields']['summary']
#    print(jira_number)