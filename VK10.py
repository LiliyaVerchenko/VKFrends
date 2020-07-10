from pprint import pprint
import requests
import os

class User:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

    def __and__ (self, other_user):
        self.other_user = other_user
        return self.user_id & other_user.user_id

    def get_mutual_friends(self):
        # выводим список ID общих друзей
        mutal_user_list = requests.get('https://api.vk.com/method/friends.getMutual',
                                       params={'access_token': self.token, 'source_uid': self.user_id,
                                               'target_uid':  self.other_user.user_id,
                                               'v': '5.120'}).json()['response']
        user_link1 = []
        url = r'https://vk.com/'
        # получаем ссылку на страницы общих друзей
        for id in mutal_user_list:
            user_link = requests.get('https://api.vk.com/method/users.get',
                                 params={'access_token': self.token, 'user_ids': id, 'fields': 'domain',
                                         'v': '5.120'}).json()['response'][0]['domain']
            user_link1.append(os.path.join(url, user_link)) # получаем ссылку путем склеивания URL и domain
        for user in user_link1:
            print(user)
        return

user1 = User(user_id_1, token)
user2 = User(user_id_2, token)
user1 & user2
user1.get_mutual_friends()

