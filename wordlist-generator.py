
import itertools




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

scale = input('\033[36m[!] PROVIDE THE SCALE [eg: "4 to 8" = 4:8] : ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])

use_nouse = str(input("\n\033[36m[?] DO YOU WAN'T TO ENTER PERSONALIZED DATA [Y/N]: "))
if use_nouse == 'y':
	first_name = str(input("\n\033[36m[*] Fist Name: "))
	last_name = str(input("\n\033[36m[*] Last Name: "))
	birthday = str(input("\n\033[36m[*] Birthday: "))
	month = str(input("\n\033[36m[*] Month: "))
	year = str(input("\n\033[36m[*] Year: "))
	chrs = first_name + last_name + birthday + month + year
else:
	chrs = 'abcdefghijklmnopqrstuvwxyz'
	pass

chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'

file_name = input('\n\033[36m[!] NAME OF YOUR FILE: ')
arq = open(file_name, 'w')
if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_up])
if input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_specials])
if input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_numerics])

for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()