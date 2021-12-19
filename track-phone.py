import mechanize
from bs4 import BeautifulSoup
import sys

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

url = "https://www.findandtrace.com/trace-mobile-number-location"

br = mechanize.Browser()
br.set_handle_robots(False) # ignore robots
br.open(url)
br.select_form(name="trace")
br["mobilenumber"] = str(input("ENTER YOUR MOBILE NUMBER:"))
res = br.submit()

soup = BeautifulSoup(res.read(),'html.parser')

tbl = soup.find_all('table',class_='shop_table')

data = tbl[1].find('tfoot')
count = 0
for tr in data:
	count += 1
	if count in (2,8,10,12,14,16,20,22,24,20,22,26):	
		th = tr.find('th')
		td = tr.find('td')
		print(th.text,td.text)

data = tbl[0].find('tfoot')

count = 0
for tr in data:
    count += 1
    if count in(6,8):
        continue
    th = tr.find('th')
    td = tr.find('td')
    print(th,td)
    exit()

def exit():
   pass
   sys.exit()


