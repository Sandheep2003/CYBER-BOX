import csv
from hashlib import md5
import sys
from subprocess import call





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

def main():
   menu()


def menu():
    print()
    
    

    choice = input("""
    SELECT THE TYPE OF HASH TO DECRYPT.
                      1: MD5
                      2: SHA256
                      3: SHA1
                      4: EXIT

                      Please enter your choice: """)

    if choice == "1": 
        MD5()
    elif choice == "2":
        SHA256()
    elif choice == "3":
        SHA1()
    elif choice == "4":
        exit()
    else:
        print("INVALID OPTION")
        
    menu()

def MD5():
   pass
   print("**********************************************")
   print("MD5 DECRYPTION HAS BEEN SELECTED.")
   call(["python", "HASH-DECRYPTER(MD5).py"])

def SHA256():
   pass
   print("**********************************************")
   print("SHA256 DECRYPTION HAS BEEN SELECTED.")
   call(["python", "HASH-DECRYPTER(sha256).py"]) 

def SHA1():
   pass
   print("**********************************************")
   print("SHA1 DECRYPTION HAS BEEN SELECTED.") 
   call(["python", "HASH-DECRYPTER(sha1).py"])
def exit():
   pass
   print("**********************************************")
   sys.exit()

main()