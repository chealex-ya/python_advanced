import random
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from token_vk import token
from pprint import pprint
import json
from get_user_info import USER
from get_random_users import RANDOM_USERS
from get_photos import VK_Get_Photo
from photos_downloader import downloader
from send_photo import send_photo
from data_writer import datawriter

vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)


def write_msg(user_id, message, attachments = None):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, 'attachment': attachments, 'random_id': randrange(10 ** 7),})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text

            if request == "привет":
                # Собираем данные пользователя
                user = USER()
                result_user = user.get_info(event.user_id)
                name = result_user[0]
                city = result_user[1]
                year = result_user[2]
                status = result_user[3]
                gender = result_user[4]

                write_msg(event.user_id, f"Привет {name}, сейчас найду тебе пару")

                # Находим соучайного пользователя
                other_users = RANDOM_USERS()
                result_other_users = other_users.get_users(city, year, status, gender)
                count = int(result_other_users['response']['count'])-1
                rand_count = random.randrange(1,count,1)
                random_person = result_other_users['response']['items'][rand_count]
                random_id = random_person['id']
                write_msg(event.user_id, f"Вот твой герой: https://vk.com/id{random_id}")
                write_msg(event.user_id, f"Ща покажу фотки")

                # Собираем фотографии случайного пользователя
                random_person = VK_Get_Photo()
                list_of_urls = random_person.get_photo(random_id)

                if list_of_urls == 'private account':
                    write_msg(event.user_id, f"пользователь запретил качать фотки((")
                    datawriter(event.user_id, random_id, 'Null', 'Null', 'Null')

                elif list_of_urls == 'Мало фоток':
                    write_msg(event.user_id, f"фоток мало, посмотри сам в профиле пользователя")
                    datawriter(event.user_id, random_id, 'Null', 'Null', 'Null')

                else:
                    for i in list_of_urls:
                        res = send_photo(event.user_id, i, vk_session)
                    a = "'"
                    b = "'"
                    photo1 = str(list_of_urls[0])
                    photo2 = str(list_of_urls[1])
                    photo3 = str(list_of_urls[2])
                    res_str1 = "%s %s %s" %(a, photo1, b)
                    res_str2 = "%s %s %s" % (a, photo2, b)
                    res_str3 = "%s %s %s" % (a, photo3, b)

                    datawriter(event.user_id, random_id, res_str1, res_str2, res_str3)


            elif request == "пока":
                write_msg(event.user_id, "Пока((")

            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")