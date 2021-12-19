import argparse
import requests, json
import sys
from sys import argv
import os


yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
green= '\033[32m'

print (yellow+"""
   _______  ______  __________     ____  ____ _  __
  / ____\ \/ / __ )/ ____/ __ \   / __ )/ __ | |/ /
 / /     \  / __  / __/ / /_/ /  / __  / / / |   / 
/ /___   / / /_/ / /___/ _, _/  / /_/ / /_/ /   |  
\____/  /_/_____/_____/_/ |_|  /_____/\____/_/|_|       
""")


ipaddress= str(input("ENTER YOUR IP ADDRESS:"))


ip = ipaddress

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
       
        print ( green+"[Victim]:", data['query'])
        print(yellow+" \u003E\u003C"*10)
        print ( green+"[ISP]:", data['isp'])
        print(yellow+" \u003E\u003C"*10)
        print ( green+"[Organisation]:", data['org'])
        print(yellow+" \u003E\u003C"*10)
        print ( green+"[City]:", data['city'])
        print(yellow+" \u003E\u003C"*10)
        print ( green+"[Region]:", data['region'])
        print(yellow+" \u003E\u003C"*10)
        print ( green+"[Time zone]:", data['timezone'])
        print(yellow+" \u003E\u003C"*10)
        print ( green+"[Zip code]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Done!!, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print ("[~]"+" check your internet connection!"+clear)
sys.exit(1)