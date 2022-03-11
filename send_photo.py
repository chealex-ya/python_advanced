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


# message = 'Зацени фотки'

# def upload_photo(upload, photo):
#     response = upload.photo_messages(photo)[0]
#
#     owner_id = response['owner_id']
#     photo_id = response['id']
#     access_key = response['access_key']
#
#     return owner_id, photo_id, access_key
#
# PEER_ID = '-211011047'
#
# def send_photo(vk, peer_id, owner_id, photo_id, access_key):
#     attachment = f'photo{owner_id}_{photo_id}_{access_key}'
#     vk.messages.send(
#         random_id=get_random_id(),
#         peer_id=peer_id,
#         attachment=attachment
#     )
#
# def main():
#     vk_session = VkApi(token=token)
#     vk = vk_session.get_api()
#     upload = VkUpload(vk)
#
#     send_photo(vk, PEER_ID, *upload_photo(upload, 'img.jpg'))
#
# if __name__ == '__main__':
#     main()


