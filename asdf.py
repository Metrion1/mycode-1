#!/usr/bin/python3

import requests

url= "http://api.open-notify.org/iss-now.json"

response= requests.get(url)
if response == "<Response [200]>":
    print("You've made contact!")

else:
    print("you suck!")
