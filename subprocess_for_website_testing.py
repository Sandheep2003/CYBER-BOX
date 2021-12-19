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
    print("************WELCOME TO CYBER BOX**************")
    print()
    
    

    choice = input("""
                      1: WEBSITE SCAN  
                      2: CLICKJACKING
                      3: REVERSE-IP
                      4: PORT SCANNER
                      5: EXIT

                      Please enter your choice: """)

    if choice == "1": 
        SCAN()
    elif choice == "2":
        CLICKJACKING()
    elif choice == "3":
        REVERSEIP()
    elif choice == "4":
        PORT()    
    elif choice == "5":
        exit()
    else:
        print("INVALID OPTION")
        
    menu()

def SCAN():
   pass
   print("**********************************************")
   print("WEBSITE SCAN HAS BEEN SELECTED.")
   call(["python", "website-scan.py"])

def CLICKJACKING():
   pass
   print("**********************************************")
   print("CLICKJACKING HAS BEEN SELECTED.")
   call(["python", "clickjacking.py"]) 
def REVERSEIP():
   pass
   print("**********************************************")
   print("REVERSE-IP HAS BEEN SELECTED.") 
   call(["python", "reverse-ip.py"])

def PORT():
   pass
   print("**********************************************")
   print("PORT_SCANNER HAS BEEN SELECTED.") 
   call(["python", "port-scanner.py"])   
def exit():
   pass
   print("**********************************************")
   sys.exit()

main()