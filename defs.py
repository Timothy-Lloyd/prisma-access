import requests
import vars
import json

def get_token():
    global token
    url = 'https://auth.apps.paloaltonetworks.com/oauth2/access_token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = 'grant_type=client_credentials&scope=tsg_id:' + vars.tsgid
    response = requests.post(
        url,
        headers=headers,
        data=data,
        auth=(vars.clientid, vars.clientsecret),
    )
    output=json.loads(response.text)
    token = output['access_token']
    
    if response.status_code != 200:
        print('error: ' + str(response.status_code))
    else:
        return token

token = get_token()
payload={}
headers = {
'Accept': 'application/json',
'Authorization': 'Bearer ' + token
}

def get_running_config():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/config-versions/running"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

def get_config():
    #currently set as version 33
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/config-versions/33"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

def list_candidate():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/config-versions"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

def get_mu_post_security_rules():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/security-rules?position=pre&folder=Mobile Users"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

#list_candidate()
#get_config()
#get_running_config()
#get_mu_post_security_rules()
