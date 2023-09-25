from session import get_session
import json
from datetime import datetime
from session import BASE_URL
response = get_session()

# json_data = json.loads(response.text)

final = []
if response.status_code == 200:
    json_data = json.loads(response.text)

    # Iterate through the issues and extract the desired fields
    for issue in json_data['issues']:
        jira_number = issue['key']
        description = issue['fields']['summary']
        ticket_link = f"{BASE_URL}/browse/{jira_number}"
        status = issue['fields']['status']['name']
        priority = issue['fields']['priority']['name']
        created_date = datetime.strptime(issue['fields']['created'], "%Y-%m-%dT%H:%M:%S.%f%z").date()
        updated_date = datetime.strptime(issue['fields']['updated'], "%Y-%m-%dT%H:%M:%S.%f%z").date()
        # comments = issue['fields']['comment']['comments']
        # latest_comment = comments[-1]['body'] if comments else "No comments"

        # Get the reporter
        reporter = issue['fields']['reporter']['displayName']

        data = {
            "Jira Number": jira_number,
            "Description": description,
            "Ticket Link": ticket_link,
            "Status": status.upper(),
            "Priority": priority,
            "Created Date": created_date,
            "Updated Date": updated_date,
            "Reporter": reporter
        }
        final.append(data)
        # Print the extracted fields
        print("Jira Number:", jira_number)
        print("Description:", description)
        print("Ticket Link:", ticket_link)
        print("Status:", type(status))
        print("Priority:", priority)
        print("Created Date:", created_date)
        print("Updated Date:", updated_date)
        # print("Latest Comment:", latest_comment)
        print("Reporter:", reporter)
        print("\n")
else:
    print("Error:", response.status_code)