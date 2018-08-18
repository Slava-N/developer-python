import requests
import time
import progressbar
import json

try:
    import token_data
    access_token = token_data.token

except:
    access_token = input("Please, enter token:\n")


api_ver='5.80'

class Session(object):

    def __init__(self, access_token, api_ver):
        self.access_token = access_token
        self.api_ver = api_ver
        print('Auth data received')

class User(object):

    def __init__(self, session, id):

        self.id = id
        params = dict(user_ids=self.id,
                      access_token=session.access_token,
                      v=session.api_ver)

        response = requests.get('https://api.vk.com/method/users.get', params)
        user_data = response.json()['response'][0]
        self.id = user_data['id']
        self.name = user_data['first_name']
        self.surname = user_data['last_name']
        self.base_params = dict(user_id=self.id,
                                access_token=session.access_token,
                                v=session.api_ver)
        print('User # {0} has been found. Name: {1}, Surname: {2}'.format(self.id, self.name, self.surname))

    def get_groups(self):
        additional_params = dict(extended=0,
                                 count=1000,
                                 user_id=self.id)
        params = {**self.base_params, **additional_params}
        response = requests.get('https://api.vk.com/method/groups.get', params)
        self.user_groups = set(response.json()['response']['items'])
        print('Target person groups are {}. Total #: {}'.format(self.user_groups, len(self.user_groups)))
        return self.user_groups

    def get_friends(self):
        response = requests.get('https://api.vk.com/method/friends.get', self.base_params)
        self.friends = response.json()['response']['items']
        return self.friends

class Query(object):


    def get_groups(self, person_id, session):
        self.person_id = person_id
        self.access_token = session.access_token
        self.api_ver = session.api_ver
        self.params = dict(user_id=self.person_id,
                           access_token=self.access_token,
                           v=self.api_ver,
                           extended=0,
                           count=1000)
        response = requests.get('https://api.vk.com/method/groups.get', self.params)
        try:
            self.user_groups = set(response.json()['response']['items'])
        except KeyError:
            self.user_groups = set()
            print('\n', response.json()['error']['error_msg'])
        return self.user_groups

    def get_groups_info(self, session, groups_ids):
        self.access_token = session.access_token
        self.api_ver = session.api_ver
        groups=','.join([str(each) for each in groups_ids])
        self.params = dict(access_token=self.access_token,
                           v=self.api_ver,
                           group_ids=groups,
                           fields='name,id,members_count')
        response = requests.get('https://api.vk.com/method/groups.getById', self.params)
        return response.json()['response']

    def execute_groups(self, people_list, session):

        self.access_token = session.access_token
        self.api_ver = session.api_ver
        person_bucket = ','.join([str(each) for each in people_list])

        code_execute = """
                var persons = (Args.person_list).split(",");
                var group_list = [];
                var i = 0;

                while (i <persons.length)
                {var person_groups = API.groups.get(
                {"user_id":persons[i]});
                i=i+1;
                group_list.push(person_groups.items);
                };
                return group_list;"""

        self.params = dict(access_token=self.access_token,
                           v=self.api_ver,
                           person_list=person_bucket,
                           code=code_execute)



        response = requests.get('https://api.vk.com/method/execute', self.params)
        # print(response.url)
        try:
            result = response.json()['response']
        except KeyError:
            result = []
        return result

if __name__ == '__main__':
    session_1 = Session(access_token, api_ver)
    target_person = User(session=session_1, id='eshmargunov') # eshmargunov, 171691064
    target_groups = target_person.get_groups()
    target_friends = target_person.get_friends()

    all_users_groups = set()
    execute_query = Query()

    for i in progressbar.progressbar(range(0,len(target_friends), 20)):
        time.sleep(1 / 2.9)
        people_bucket = target_friends[i:i+20]
        groups_bucket = execute_query.execute_groups(people_bucket, session_1)
        # print(groups_bucket)
        clean_groups_bucket = [each for each in groups_bucket if each != None]
        all_users_groups.update(*clean_groups_bucket)

    time.sleep(2)

    unique_groups = target_groups.difference(all_users_groups)

    print('\nUnique groups are:\n{}'.format(unique_groups))
    unique_groups_info = Query()
    unique_groups_info_file = unique_groups_info.get_groups_info(session_1, list(unique_groups))

    with open('groups.json', 'w', encoding='UTF-8') as outfile:
        json.dump(unique_groups_info_file, outfile, ensure_ascii=False)





