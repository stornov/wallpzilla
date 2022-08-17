import requests
from bs4 import BeautifulSoup as bs


def getImageFile():
	URL = 'https://www.bing.com'
	r = requests.get(URL)
	soup = bs(r.text, 'html.parser')

	temp = soup.find('div', class_='img_cont')['style']
	image_url = temp[temp.find('/'):temp.find(';')-1]

	temp = image_url[image_url.find('id=')+3:image_url.find('.jpg')]
	short_name = temp[temp.find('.')+1:temp.find('_')]

	image_data = requests.get(URL+image_url).content
	with open(f'wallpapers/{image_name}.jpg', 'wb') as file:
		file.write(image_data)


getImageFile()