import requests
import token_data

access_token = token_data.token
api_ver='5.80'

class Session(object):

    def __init__(self, access_token, api_ver):
        self.access_token = access_token
        self.api_ver = api_ver
        print('Auth data received')


class User(object):

    def __init__(self, id, session):
        self.id = id
        self.params = dict(user_id=id,
                      access_token=session.access_token,
                      v=session.api_ver)
        response = requests.get('https://api.vk.com/method/users.get', self.params)
        user_data = response.json()['response'][0]
        self.name = user_data['first_name']
        self.surname = user_data['last_name']
        print('User # {0} has been found. Name: {1}, Surname: {2}'.format(self.id, self.name, self.surname))

    def __str__(self):
        return "vk.com/id{}".format(self.id)

    def get_friends(self):
        response = requests.get('https://api.vk.com/method/friends.get', self.params)
        return (response.json()['response']['items'])

    def __and__(self, other):
        self.get_friends()
        print(set(self.get_friends()).intersection(other.get_friends()))
        return set(self.get_friends()).intersection(other.get_friends())

session_1 = Session(access_token, api_ver)

user_1 = User('1946565', session_1)
user_2 = User('179095856', session_1)

print(user_2)
user_1 & user_2
