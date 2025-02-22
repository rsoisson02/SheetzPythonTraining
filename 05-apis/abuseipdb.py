
# -*- coding: utf-8 -*-
"""

Open the JSON log file titled "network_traffic.json". Write a program that will:
    1. Pull all of the IP addresses from the log
    2. Send each IP address to the abuseIPDB API
    3. Determine whether or not the IP has been flagged for abuse (abuseConfidenceScore > 0)
    4. Add all flagged IPs to a dictionary with the IP being the key, and the abuseConfidenceScore
       being the value
    5. Print the dictionary. 

"""

import requests
from pprint import pprint
import json

url = "https://api.abuseipdb.com/api/v2/check/"
headers = {
  'Key': '2da6b3b57dbffdf98880bad799338b21328eb9077ce8aeb1d7d2fc32e87c7cea21fa5af9caea1d7c'
}
ip_dictionary = {}
ip_list = []


# Open the JSON log file


# Append the IP Addresses from the log file to the list


for ip in ip_list:
    payload = {"ipAddress": ip}

    # Finish the for loop by making the request, checking the abusescore, and adding the IP to the dictionary if it is flagged


