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
                      1: WORDLIST GENERATOR
                      2: HASH ENCRYPTER
                      3: HASH DECRYPTER
                      4: HASH IDENTIFIER
                      5: EXIT

                      Please enter your choice: """)

    if choice == "1": 
        WORDLIST()
    elif choice == "2":
        ENCRYPTER()
    elif choice == "3":
        DECRYPTER()
    elif choice == "4":
        IDENTIFIER()        
    elif choice == "5":
        exit()
    else:
        print("INVALID OPTION")
        
    menu()

def WORDLIST():
   pass
   print("**********************************************")
   print("WORDLIST GENERATOR HAS BEEN SELECTED.")
   call(["python", "wordlist-generator.py"])

def ENCRYPTER():
   pass
   print("**********************************************")
   print("WORDLIST GENERATOR HAS BEEN SELECTED.")
   call(["python", "subprocess_for_encrypter.py"])

def DECRYPTER():
   pass
   print("**********************************************")
   print("HASH DECRYPTER GENERATOR HAS BEEN SELECTED.")
   call(["python", "subprocess_for_decrypter.py"])

def IDENTIFIER():
   pass
   print("**********************************************")
   print("HASH IDENTIFIER HAS BEEN SELECTED.")
   call(["python", "HASH-IDENTIFIER.py"])


def exit():
   pass
   print("**********************************************")
   sys.exit()

main()