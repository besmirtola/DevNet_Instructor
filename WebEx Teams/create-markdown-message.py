# Fill in this file with the messages code from the Webex Teams exercise
import requests


access_token = 'ZGI1Y2NiNGYtYTNlYy00YjQzLWFlYmMtZTM0ZWI1ZTk2YzdhMDQwMjA1NTUtNTIz_PF84_2ec9c128-5f70-44f0-ac34-595d586542bb'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vYmVlZjk5NTAtZjMxYy0xMWVjLWJmYzItYjE5ZDg0ZGMwNWY2'
message = "https://github.com/besmirtola/DevNet_Skills.git"
url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())