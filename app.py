from simple_salesforce import Salesforce, format_soql
from pprint import pprint
import json


# open file holding our login information
# we have the login info in a separate file so we can
# add it to .gitignore to help prevent leaking the information
# environment variables could also work
with open("login.json", "r") as login_file:
    creds = json.load(login_file)

sf = Salesforce(username=creds['login']['username'],
                password=creds['login']['password'],
                security_token=creds['login']['token'])




# an example of running a simple SOQL query
SOQL = "SELECT Id, Email FROM Contact"
data = sf.query(SOQL)
for d in data['records']:
    pprint(f"{d['Id']} -- {d['Email']}")

input("Script Paused...")




# generate some mock data
# heres an example on list comprehension:
#     data = [{'Name': f"Bulk Test {i}"} for i in range(0, 1000)]
# but a simple for loop is easier to understand
data = []
for i in range(0,1000):
    data.append({
        "Name": f"Bulk Test {i}"
    })
pprint(data)

input("Script Paused...")




# insert the new account using the bulk api
x = sf.bulk.Account.insert(data, batch_size=10000, use_serial=True)
pprint(x)

input("Script Paused...")




# now lets get those records so we can delete them
SOQL = format_soql("SELECT Id, Name FROM Account WHERE Name LIKE '{:like}%'", "Bulk Test")
the_accounts = sf.bulk.Account.query(SOQL)
pprint(the_accounts)

input("Script Paused...")



# now we'll get just the Id's to pass to bulk delete
# we don't need the attributes, only the Id's
# heres an example on list comprehension:
#     account_ids = [{"Id": a["Id"]} for a in the_accounts]
# but a simple for loop is easier to understand
account_ids = []
for a in the_accounts:
    account_ids.append({"Id": a["Id"]})
pprint(account_ids)

input("Script Paused...")




# delete the records
data = sf.bulk.Account.delete(account_ids, batch_size=10000, use_serial=True)
pprint(data)

print("End Script =)")