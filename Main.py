import csv
import sys
import os
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

a = 10
b = 20

def main():
   menu()


def menu():
    print("************WELCOME TO CYBER BOX**************")
    print()
    
    

    choice = input("""
                      1: INFORMATION GATHERING
                      2: WEBSITE TESTING
                      3: ATTACKS
                      4: EXIT

                      Please enter your choice: """)

    if choice == "1":
        INFORMATION()
    elif choice == "2":
        WEBSITE()
    elif choice == "3":
        ATTACKS()
    elif choice == "4":
        exit()
    else:
        print("INVALID OPTION")
        
    menu()
    


def INFORMATION():
   pass
   print("**********************************************")
   print("INFORMATION GATHERING HAS BEEN SELECTED.")
   call(["python", "subprocess_for_information.py"])
    
def WEBSITE():
   pass
   print("**********************************************")
   print("WEBSITE TESTING HAS BEEN SELECTED.")
   call(["python", "subprocess_for_website_testing.py"])
def ATTACKS():
   pass
   print("**********************************************")
   print("ATTACKS HAS BEEN SELECTED.") 
   call(["python", "subprocess_for_attacks.py"])
def exit():
   pass
   print("**********************************************")
   sys.exit(print("THANK YOU FOR USING THE TOOL."))

clear= lambda: os.system("cls")

main()


