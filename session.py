import requests
import json
import base64
import pprint

BASE_URL = 'https://goclick.atlassian.net'

def get_session():
   cred =  "Basic " + base64.b64encode(b'syasar-vendor@clicktherapeutics.com:ATATT3xFfGF0UTq41AWQmaWlzgZnbSNSuT8NoA9bWdER_xm6exql3GZUEJoyZbyWXMgDjJkMsPO26C_MasnEvruUoRv5_-DiDToRHEcYaqDLyYqUDtT0c060SiOzpFrFGVqYWUaUOS3UEGLsGioht8r60i5KemouT48AkhOXBHI5vPDZx5jZeW4=DD889EB7').decode("utf-8") 

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

# json_data = json.loads(response.text)

# pprint.pprint(json_data['issues'][0]['fields'])

# for issue in json_data['issues']:
#    jira_number = issue['key']
#    description = issue['fields']['summary']
#    print(jira_number)