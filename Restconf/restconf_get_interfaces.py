### RESTCONF INTERFACES GET POST PUT DELETE
### OPTIONS
###### GET Read
###### PATCH Update
###### PUT Create or Replace
###### POST Create or Operations (reload, default) ==> you can only POST once (on creation)!
###### DELETE Deletes the targeted resource
###### HEAD Header metadata (no response body)
###
import datetime
import requests
import json
import urllib3


print ("Current date and time: ")
print(datetime.datetime.now())

# Disable SSL Verification Warning because of Private SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#requests.packages.urllib3.disable_warnings()
#dir(requests)
#dir(json)


print('Creating request and necessary variables')
print('-------Step 1 (Router IP)-------')
router_ip = "192.168.56.101" ### check ip address of local virtual router
print("Router IP: " + router_ip)

print('-------Step 2 (API URL)-------')
api_url = "https://{0}/restconf/data/ietf-interfaces:interfaces".format(router_ip)
print("restconf url: " + api_url)

print('-------Step 3 (Request Headers)-------')
# A mistake in the headers generates an HHTP ERROR 406 Not Acceptable
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
print(headers)

print('-------Step 4 (Authentication)-------')
#A wrong password will generate HTTP ERROR 401 Unauthorized
basicauth =('cisco', 'cisco123!')
print(basicauth)

print('-------5 (HTTP Method)-------')
print('=> Sending GET request for information interfaces')
# Remark: Dynamic DHCP Address not shown
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {}'.format(resp.status_code,resp.json()))

# Print a stream of bytes as pretty JSON
def printBytesAsJSON(bytes):
	print(json.dumps(json.loads(bytes), indent=2))

# Pretty print our JSON response
print("-------6 (Pretty Print of JSON)------")
printBytesAsJSON(resp.content)

