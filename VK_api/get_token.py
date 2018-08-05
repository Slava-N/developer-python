import requests
from urllib.parse import urlencode, urlparse
from time import sleep
import json

app_id = 6652821
auth_url = 'https://oauth.vk.com/authorize'
api_ver = '5.80'

auth_data = dict(client_id=app_id,
                 redirect_uri='https://oauth.vk.com/blank.html',
                 display='page',
                 scope='friends, status',
                 response_type='token',
                 v=api_ver)

print('?'.join([auth_url, urlencode(auth_data)]))
