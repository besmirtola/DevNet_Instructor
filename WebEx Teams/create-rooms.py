# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests



access_token = 'ZGI1Y2NiNGYtYTNlYy00YjQzLWFlYmMtZTM0ZWI1ZTk2YzdhMDQwMjA1NTUtNTIz_PF84_2ec9c128-5f70-44f0-ac34-595d586542bb'
url = 'https://webexapis.com/v1/rooms'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

params={'title': 'devasc_skills_BT'}
res = requests.post(url, headers=headers, json=params)
print(res.json())