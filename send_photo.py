from vk_api.longpoll import VkLongPoll, VkEventType
from token_vk import token
from vk_api import VkUpload
import requests
from random import randrange



def send_photo(user_id, image_url, vk_session):
    session = requests.Session()
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)
    attachments = []
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append(
        'photo{}_{}'.format(photo['owner_id'], photo['id'])
    )
    vk.messages.send(
        user_id= user_id,
        random_id= randrange(10 ** 7),
        attachment=','.join(attachments)
    )




