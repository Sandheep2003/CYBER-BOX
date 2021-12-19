from hashlib import sha1

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

hash_value = input("ENTER THE HASH VALUE(SHA1): ")
wordlist = ['sandheep','pavan','arthi','neha','password']

flag=False
val=""
for word in wordlist:
    value = sha1(word.encode())
    if hash_value == value.hexdigest():
        flag=True
        val=word
        break

if flag:
    print("THE HASH VALUE IS:",val)
else:
    print("Not possible")