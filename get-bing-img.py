import requests
from bs4 import BeautifulSoup as bs
import os.path


def getImageFile():
	URL = 'https://www.bing.com'
	r = requests.get(URL)
	soup = bs(r.text, 'html.parser')

	temp = soup.find('div', class_='img_cont')['style']
	image_url = temp[temp.find('/'):temp.find(';')-1]

	temp = image_url[image_url.find('id=')+3:image_url.find('.jpg')]
	image_name = temp[temp.find('.')+1:temp.find('_')]
	if os.path.isfile(f'wallpapers/{image_name}.jpg'):
		return False


	image_data = requests.get(URL+image_url).content
	with open(f'wallpapers/{image_name}.jpg', 'wb') as file:
		file.write(image_data)
	return True