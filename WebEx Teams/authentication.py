# Fill in this file with the authentication code from the Webex Teams exercise
import requests
import json


access_token = 'ZGI1Y2NiNGYtYTNlYy00YjQzLWFlYmMtZTM0ZWI1ZTk2YzdhMDQwMjA1NTUtNTIz_PF84_2ec9c128-5f70-44f0-ac34-595d586542bb'
url = 'https://webexapis.com/v1/people/me'
headers = {'Authorization': 'Bearer {}'.format(access_token)}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

