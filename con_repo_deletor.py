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

def tags_deletor(access_token, prj_id, reg_id, name_regex_delete, keep_n, older_than, name_regex_keep):
    data = {'name_regex_delete': name_regex_delete,'keep_n': keep_n, 'older_than': older_than, 'name_regex_keep': name_regex_keep}
    response = requests.delete("https://gitlab.com/api/v4/projects/{prj_id}/registry/repositories/{reg_id}/tags".format(prj_id=prj_id, reg_id=reg_id), data=data, headers = {'Private-Token': access_token})
    response_status = str(response)
    response_msg = json.loads(response.text)
    if response_status == "<Response [202]>":
        print("Successfully deleted")
        logging.info('Status code: 202 \t Deletion of Tags in the Container Registry was Successful')
    elif response_status == "<Response [400]>":
        logging.error('Status code: 400 \t ' + response_msg['message'])
    else:
        logging.critical('Unknown Error please troubleshoot and run the program again')

def main():
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
        print("Procesing Image Tags......")
        tags_deletor(access_token, prj_id, reg_id, name_regex_delete, keep_n, older_than, name_regex_keep)

