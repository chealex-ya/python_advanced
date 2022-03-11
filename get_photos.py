import requests
from token_vk import access_token
from pprint import pprint


class VK_Get_Photo:
    url = 'https://api.vk.com/method/'
    def __init__(self):
        self.params = {
            'access_token': access_token,
            'v': '5.131'
        }

    def get_photo(self, id):
        owner_id = id
        url_get_photo = self.url + 'photos.get'
        get_photo_params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': '1'
        }
        res = requests.get(url_get_photo, params={**self.params, **get_photo_params}).json()

        try:
            count = int(res['response']['count'])-1
            my_photos_dict = {}

            if count > 49:
                for i in range(0, 50):
                    my_photos_dict[i] = (res['response']['items'][i]['comments']['count'] + res['response']['items'][i]['likes']['count'])

            elif count < 3:
                return 'Мало фоток'

            else:
                for i in range(0, count):
                    my_photos_dict[i] = (res['response']['items'][i]['comments']['count'] + res['response']['items'][i]['likes']['count'])


            best_photos_list = []

            x = 0
            for k,v in sorted(my_photos_dict.items(), key=lambda x: x[1], reverse=True):
                if x < 3:
                    try:
                        best_photos_list.append(res['response']['items'][k]['sizes'][0]['url'])
                        x += 1
                    except ValueError:
                        return best_photos_list

            return best_photos_list
        except KeyError:
            return 'private account'

# test = VK_Get_Photo()
# res = test.get_photo('306683')
#
# random_person = VK_Get_Photo()
# list_of_urls = random_person.get_photo('102854')
# print(random_person)
# print(list_of_urls)