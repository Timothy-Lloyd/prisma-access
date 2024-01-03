import requests
import vars
import json
import time
import os
import json

localtime = time.localtime()
formattime = time.strftime("%d-%m-%Y %H:%M:%S", localtime)
datetime = time.strftime("%d-%m-%Y", localtime)

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
headersPost = {
'Content-Type': 'application/json',
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

def get_shared_post_security_rules():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/security-rules?position=post&folder=Shared"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    with open(os.path.join("output/shared_post_security_rules.json"), "a") as file:
        json.dump(response.json(), file)
def put_shared_post_security_rules():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/security-rules?position=post&folder=Shared"
    with open(os.path.join("output/shared_post_security_rules.json"), "r") as file:
        payload = json.load(file)
    response = requests.request("POST", url, headers=headersPost, json=payload)
    print(response.text)

def get_global_url_access_profiles():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/url-access-profiles?folder=Shared"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    with open(os.path.join("output/global_url_access_profile.json"), "a") as file:
        json.dump(response.json(), file)
def put_global_url_access_profiles():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/url-access-profiles?folder=All"
    with open(os.path.join("output/global_url_access_profile.json"), "r") as file:
        payload = json.load(file)
    response = requests.request("POST", url, headers=headersPost, json=payload)
    print(response.text)
 
def get_global_file_blocking_profiles():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/file-blocking-profiles?folder=Shared"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    with open(os.path.join("output/global_file_blocking_profile.json"), "a") as file:
        json.dump(response.json(), file)
def put_global_file_blocking_profiles():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/file-blocking-profiles?folder=All"
    with open(os.path.join("output/global_file_blocking_profile.json"), "r") as file:
        payload = json.load(file)
    response = requests.request("POST", url, headers=headersPost, json=payload)
    print(response.text)
 
def get_global_objects_services():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/services?folder=Shared"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    with open(os.path.join("output/global_objects_services.json"), "a") as file:
        json.dump(response.json(), file)
def put_global_objects_services():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/services?folder=All"
    with open(os.path.join("output/global_objects_services.json"), "r") as file:
        payload = json.load(file)
    response = requests.request("POST", url, headers=headersPost, json=payload)
    print(response.text)


#list_candidate()
#get_config()
#get_running_config()
#get_shared_post_security_rules()
#put_shared_post_security_rules()
#get_global_url_access_profiles()
#put_global_url_access_profiles()
#get_global_file_blocking_profiles()
#put_global_file_blocking_profiles()
#get_global_objects_services()
#put_global_objects_services()
