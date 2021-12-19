import hashlib

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


mystring = input("\033[32mENTER THE TEXT TO ENCRYPT IN MD5: ")
hash_object = hashlib.md5(mystring.encode())
print("")
print("CONVERTED HASH VALUE IS:",hash_object.hexdigest())
print("")
	