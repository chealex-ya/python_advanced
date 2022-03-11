import requests

def downloader(img):
	p = requests.get(img)
	out = open('/Users/ruachaj/PycharmProjects/pythonProject1/venv/Course_advance/img.jpg', "wb")
	out.write(p.content)
	out.close()


