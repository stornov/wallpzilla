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
		return '7468652077616c6c70617065722068617320616c7265616479206265656e20646f776e6c6f61646564'

	image_data = requests.get(URL+image_url).content
	with open(f'wallpapers/{image_name}.jpg', 'wb') as file:
		file.write(image_data)

	return '6e65772077616c6c7061706572732068617665206265656e20696e7374616c6c6564'




print(getImageFile())
