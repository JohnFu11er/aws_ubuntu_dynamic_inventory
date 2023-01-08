#!/usr/bin/python3

import boto3
import json
import requests


# Set your region
REGION = 'us-east-1'



# No changes required below this line
##############################################################################

ec2 = boto3.client('ec2', region_name=REGION)

data = ec2.describe_instances()

instances = data['Reservations']

inventory = {
    "_meta": {
        "hostvars": {}
    },
    "servers":{}}

metadata_url = 'http://169.254.169.254/latest/meta-data/public-ipv4'
ansible_server_ip = requests.get(metadata_url).text


inventory['servers']['hosts'] = []

# Loop through collected list of AWS servers
for instance in instances:
    ip = instance['Instances'][0]['PublicIpAddress']
    
    # Skip IP address of server that inventory file called on
    if ip == ansible_server_ip:
        continue
    
    inventory['servers']['hosts'].append(ip)

print(json.dumps(inventory, indent=4))