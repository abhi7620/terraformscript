/* Fetch List of server from AWS and groups based on ec2 instance tag name and value */

import print
import boto3
import json

def getgrouphosts(ec2):
    allgroups = {}
	
	for each_in in ec2.instance.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
		for tag in each_in.tags:
		    if tag["key"] in allgroups:
				hosts = allgroups.get(tag["key"])
				hosts.append(each_in.public_ip_address)
				allgroups[tag["key"]] = hosts
			else:
				hosts = [each_in.public_ip_address]
				allgroups[tag["key"]] = hosts
			if  tag["value"] in allgroups
               	hosts = allgroups.get(tag["value"])
				hosts.append(each_in.public_ip_address)
				allgroups[tag["value"]] = hosts		
			else:
				hosts = [each_in.public_ip_address]
				allgroups[tag["value"]] = hosts	
				
	return allgroups;

def main()
	ec2 = boto3.resource('ec2')
    all_groups = getgroupofhosts(ec2)
	inventory = {}
	for key, value in all_groups.items();
		hostsobj = {'hosts': value}
		inventory[key] = hostsobj
	print(json.dumps(inventory))

if __name__ == "__main__":
	main()	