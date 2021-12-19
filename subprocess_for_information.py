import csv
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
                      1: SOCIAL MEDIA INFORMATION GATHERING
                      2: MOBILE NUMBER INFORMATION GATHERING
                      3: IP-ADDRESS INFORMATION GATHERING
                      4: EXIT

                      Please enter your choice: """)

    if choice == "1": 
        SOCIAL()
    elif choice == "2":
        MOBILE()
    elif choice == "3":
        IP()
    elif choice == "4":
        exit()
    else:
        print("INVALID OPTION")
        
    menu()

def SOCIAL():
   pass
   print("**********************************************")
   print("SOCIAL MEDIA INFORMATION GATHERING HAS BEEN SELECTED.")
   call(["python", "Social Media.py"])

def MOBILE():
   pass
   print("**********************************************")
   print("MOBILE NUMBER INFORMATION GATHERING HAS BEEN SELECTED.")
   call(["python", "track-phone.py"]) 
def IP():
   pass
   print("**********************************************")
   print("IP-ADDRESS INFORMATION GATHERING HAS BEEN SELECTED.") 
   call(["python", "IP-info.py"])
def exit():
   pass
   print("**********************************************")
   sys.exit()

main()