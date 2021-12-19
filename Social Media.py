'''imports'''
import requests
import time
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
''' INPUT USERNMAE OF TARGET '''
username = input('\033[92m ENTER USERNAME OF TARGET: ')


# FACEBOOK
facebook = f'https://www.facebook.com/{username}'

# INSTAGRAM
instagram = f'https://www.instagram.com/{username}'

# TWITTER
twitter = f'https://www.twitter.com/{username}'

# YOUTUBE

youtube = f'https://www.youtube.com/c/{username}'

# GITHUB
github = f'https://www.github.com/{username}'

# STEAM
steam = f'https://steamcommunity.com/id/{username}'

# MEDIUM
medium = f'https://medium.com/@{username}'

# SPOTIFY
spotify = f'https://open.spotify.com/user/{username}'

''' WEBSITE LIST '''
WEBSITES = [
facebook, instagram, twitter, youtube, github, steam,
medium, spotify,
]


''' COLOUR FUNCTION '''
def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function


''' COLOUR PRINTS '''
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')


''' BANNER '''
def banner():
    GREEN(r'''
   _______  ______  __________     ____  ____ _  __
  / ____\ \/ / __ )/ ____/ __ \   / __ )/ __ | |/ /
 / /     \  / __  / __/ / /_/ /  / __  / / / |   / 
/ /___   / / /_/ / /___/ _, _/  / /_/ / /_/ /   |  
\____/  /_/_____/_____/_/ |_|  /_____/\____/_/|_|  
  ''')


def search():
    GREEN(f' SEARCHING FOR USERNAME:{username}')
    time.sleep(0.5)
    print('.......')
    time.sleep(0.5)
    print('.......\n')
    time.sleep(0.5)

    GREEN(f' TOOL IS WORKING \n')
    time.sleep(0.5)
    print('.......')
    time.sleep(0.5)
    print('.......\n')
    time.sleep(0.5)

    time.sleep(1)

    count = 0
    match = True
    for url in WEBSITES:
        r = requests.get(url)

        if r.status_code == 200:
            if match == True:
                GREEN('[+] FOUND MATCHES')
                match = False
            YELLOW(f'\n{url} - {r.status_code} - OK')
            if username in r.text:
                GREEN(f'{username} - USERNAME HAS BEEN DETECTED.')
            else:
                GREEN(f'{username} - USERNAME HAS NOT BEEN DETECTED.')#
        count += 1


if __name__=='__main__':
    banner()
    search()




