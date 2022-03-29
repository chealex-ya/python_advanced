import random
import requests
from token_vk import access_token
from pprint import pprint

class RANDOM_USERS:
	url = 'https://api.vk.com/method/'
	def __init__(self):
		self.params = {
			'access_token': access_token,
			'v': '5.131'
		}

	def get_users(self, city, birth_year, status, gender):
		if gender == 1:
			a_gender = 2
		else:
			a_gender = 1

		url_get_profile = self.url + 'users.search'
		get_user_params = {
			'city': city,
			'birth_year': birth_year,
			'status': status,
			'sex': a_gender,
			'has_photo': '1',
			'fields': 'city, sex, status, bdate',
			'count': '1000'
			# 'offset': random_number
		}
		random_users = requests.get(url_get_profile, params={**self.params, **get_user_params})
		return random_users.json()

