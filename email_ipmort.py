import requests
import csv

CPANEL_API_TOKEN = ''
CPANEL_USER =''
DOMAIN=''
PORT='2083'
API_ENDPOINT='/execute/Email/list_pops?regex=user'


api_url = 'https://' + DOMAIN + ':' + PORT + API_ENDPOINT
api_headers = {
    'Authorization': 'cpanel {}:{}'.format(CPANEL_USER, CPANEL_API_TOKEN),
    'Content-Type': 'application/json',
}

try:
	response = requests.get(api_url, headers=api_headers)
	data = response.json()
	print(data)
except Exception as e:
	print(e)  

accounts = data['data']
account_details = []
for account in accounts:       
    email = account['email']
    account_details.append([email])

csv_filename = 'accounts.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Email'])
    writer.writerows(account_details)

print(f"Accounts exported to {csv_filename}.")
