import requests
from token_vk import token
from pprint import pprint
from datetime import datetime


class USER:
    url = 'https://api.vk.com/method/'
    def __init__(self):
        self.params = {
            'access_token': token,
            'v': '5.131'
        }

    def get_info(self, id):
        url_get_profile = self.url + 'users.get'
        get_user_params = {
            'user_ids': id,
            'fields': 'bdate, city, sex, status'
        }
        user_profile = requests.get(url_get_profile, params={**self.params, **get_user_params})
        try:
            name = user_profile.json()['response'][0]['first_name']
        except:
            name = "No_name"
        try:
            city = user_profile.json()['response'][0]['city']['id']
        except:
            city = 2
        try:
            bdate = user_profile.json()['response'][0]['bdate']
            year_stamp = datetime.strptime(bdate, "%d.%m.%Y")
            year = datetime.date(year_stamp).year
        except:
            city = 2
        try:
            status = user_profile.json()['response'][0]['status']
        except:
            status = 1
        try:
            gender = user_profile.json()['response'][0]['sex']
        except:
            gender = 2

        return name, city, year, status, gender
