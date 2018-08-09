from urllib.parse import urlencode, urlparse


app_id = 6655967
auth_url = 'https://oauth.vk.com/authorize'
api_ver = '5.80'

auth_data = dict(client_id=app_id,
                 redirect_uri='https://oauth.vk.com/blank.html',
                 display='page',
                 scope='friends, status, groups',
                 response_type='token',
                 v=api_ver)

print('?'.join([auth_url, urlencode(auth_data)]))
