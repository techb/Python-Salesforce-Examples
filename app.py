from simple_salesforce import Salesforce
import json

# open file holding our login information
# we have the login info in a seporate file so we can
# add it to .gitignore to help prevent leaking the information
# environment variables could also work
with open("login.json", "r") as login_file:
    creds = json.load(login_file)


sf = Salesforce(username=creds['login']['username'],
                password=creds['login']['password'],
                security_token=creds['login']['token'])


SOQL = "SELECT Id, Email FROM Contact"
data = sf.query(SOQL)

for d in data['records']:
    print(f"{d['Id']} -- {d['Email']}")
