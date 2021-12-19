from urllib.request import urlopen
cyan="\033[1;36;40m"
green="\033[1;32;40m"
Y = '\033[1;33;40m'
yellow = '\033[93m'


print (yellow+"""
   _______  ______  __________     ____  ____ _  __
  / ____\ \/ / __ )/ ____/ __ \   / __ )/ __ | |/ /
 / /     \  / __  / __/ / /_/ /  / __  / / / |   / 
/ /___   / / /_/ / /___/ _, _/  / /_/ / /_/ /   |  
\____/  /_/_____/_____/_/ |_|  /_____/\____/_/|_|       
""")
def ClickJacking():
    host=input("ENTER THE TARGET: >>"+yellow)
    port=int(input("ENTER PORT: >>"+yellow))
    if port == 80:
          port = 'http://'
    elif port == 443:
          port = 'https://'
    else:
         print("Could'nt fetch data for the given PORT"+yellow)


    url = (port+host)

    data = urlopen(url)
    headers = data.info()

    if not "X-Frame-Options" in headers:
          print(green+"THIS WEBSITE IS VULNERABLE TO CLICKJACKING.")

    else:
        print("THIS WEBSITE IS NOT VULNERABLE TO CLICKJACKING.")
if __name__=="__main__":
    ClickJacking()