# testing not working also not useful in this program

import requests
from requests.auth import HTTPBasicAuth
response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('username', 'password'))

print('Response Code ' + str(response.status_code))

if response.status_code == 200:
    print('Login Sucessful: '+response.text)




