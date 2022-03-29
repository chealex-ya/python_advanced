import random
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from token_vk import token
import json
from get_user_info import USER
from get_random_users import RANDOM_USERS
from get_photos import VK_Get_Photo
from photos_downloader import downloader
from send_photo import send_photo
from data_writer import datawriter
from check_if_unique import check

if __name__ == "__main__":

    vk_session = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(vk_session)


    def write_msg(user_id, message, attachments = None):
        vk_session.method('messages.send', {'user_id': user_id, 'message': message, 'attachment': attachments, 'random_id': randrange(10 ** 7),})

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text

                if request == "Привет":
                    # Собираем данные пользователя
                    user = USER()
                    result_user = user.get_info(event.user_id)
                    name = result_user[0]
                    city = result_user[1]
                    year = result_user[2]
                    status = result_user[3]
                    gender = result_user[4]

                    write_msg(event.user_id, f"Привет {name}, сейчас найду тебе пару")

                    if city == '':
                        rand = write_msg(event.user_id, f"Косяк, я не знаю твой город. Напиши в ответ")
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW:
                                if event.to_me:
                                    city = event.text
                                    break

                    if year == '':
                        rand = write_msg(event.user_id, f"Косяк, я не знаю твой год рождения. Напиши мне в формате 1945")
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW:
                                if event.to_me:
                                    year = event.text
                                    break

                    if status == '':
                        rand = write_msg(event.user_id, f"Косяк, я не знаю твой статус. Ответь 1  - если в браке, иначе - 2")
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW:
                                if event.to_me:
                                    status = event.text
                                    break

                    if gender == '':
                        rand = write_msg(event.user_id, f"Косяк, я не знаю твой пол. Ответь 1  - если парень, и 2 - если девушка")
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW:
                                if event.to_me:
                                    gender = event.text
                                    break

                    # Находим случайного пользователя

                    other_users = RANDOM_USERS()
                    result_other_users = other_users.get_users(city, year, status, gender)
                    count = int(result_other_users['response']['count'])-1

                    # проверка, что таких пользователей ранее не выдавалосьg
                    while True:
                        rand_count = random.randrange(1,count,1)
                        random_person = result_other_users['response']['items'][rand_count]
                        random_id = random_person['id']
                        if check(random_id) == True:
                            pass
                        if check(random_id) == False:
                            break

                    write_msg(event.user_id, f"Вот твой герой: https://vk.com/id{random_id}")
                    write_msg(event.user_id, f"Ща покажу фотки")

                    # Собираем фотографии случайного пользователя
                    random_person = VK_Get_Photo()
                    list_of_urls = random_person.get_photo(random_id)

                    result = {}

                    result['user_id'] = event.user_id
                    result['other_user_id'] = random_id

                    if list_of_urls == 'private account':
                        write_msg(event.user_id, f"пользователь запретил качать фотки((")
                        result['links'] = []

                    elif list_of_urls == 'Мало фоток':
                        write_msg(event.user_id, f"фоток мало, посмотри сам в профиле пользователя")
                        result['links'] = []

                    else:
                        for i in list_of_urls:
                            res = send_photo(event.user_id, i, vk_session)
                        result['links'] = list_of_urls

                    # запись в файл
                    with open("data.json", "w") as write_file:
                        json.dump(result, write_file)

                    # запись в базу
                    try:
                        datawriter()
                    except:
                        print('Сохранил изменения во временный файл, поэтому могут быть повторы')


                elif request == "пока":
                    write_msg(event.user_id, "Пока((")

                else:
                    write_msg(event.user_id, "Не поняла вашего ответа...")