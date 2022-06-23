# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json


access_token = 'ZGI1Y2NiNGYtYTNlYy00YjQzLWFlYmMtZTM0ZWI1ZTk2YzdhMDQwMjA1NTUtNTIz_PF84_2ec9c128-5f70-44f0-ac34-595d586542bb'
url = 'https://webexapis.com/v1/people'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {
 'email': 'besmir.tola@ntnu.no'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))


person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lZTExYjJmMS03YjBiLTRmZTYtYmFiOC0wOTc2ZDk3MjhiNjE'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))