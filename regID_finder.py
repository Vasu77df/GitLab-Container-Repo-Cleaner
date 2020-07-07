#!bin/python3
import requests
import json
import pprint
from time import sleep
import logging

def image_get(access_token, prj_id):
    response = requests.get("https://gitlab.com/api/v4/projects/{prj_id}/registry/repositories".format(prj_id=prj_id), headers = {'Private-Token': access_token})
    imagels_output = response.text
    return imagels_output 

def payload_dictbuidler(payloads):
    payload = {}
    for i in range(0, len(json.loads(payloads))):
        out = json.loads(payloads)[i]
        payload['Payload {}'.format(i)] = out
    return payload
    
if __name__ == "__main__":
     with open('credentials.json') as json_file:
        data = json.load(json_file)
        access_token = data["Access-Token"]
        prj_id = data["Project ID"]
        reg_id = data["Registry ID"]
        name_regex_delete = data["name_regex_delete"]
        keep_n = data["keep_n"]
        older_than = data["older_than"]
        name_regex_keep = data["name_regex_keep"]
        dk_images = image_get(access_token, prj_id)
        images = payload_dictbuidler(dk_images)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(images)