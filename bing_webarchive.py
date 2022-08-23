import requests
from bs4 import BeautifulSoup as bs
import os


r = requests.get('https://web.archive.org/cdx/search/cdx?url=bing.com&fl=statuscode,timestamp,&output=json')


l = [i for i in eval(r.text) if i[0]=='200'][::-1]
urls = [f'https://web.archive.org/web/{i[1]}/https://www.bing.com/' for i in l][2100+1400:]

counter1 = 0
counter2 = 0
imgs = []
for i in urls:
    counter2 += 1
    r = requests.get(i)
    soup = bs(r.text, 'html.parser')
    href = soup.find('link', id='preloadBg')['href']
    image_url = href[href.find('https'):href.find('qlt')-1]
    temp = image_url[image_url.find('id=')+3:image_url.find('.jpg')]
    image_name = temp[temp.find('.')+1:temp.find('_')]
    if os.path.isfile(f'wallpapers/{image_name}.jpg'):
        if image_name not in imgs:
            imgs.append(image_name)
            counter1 += 1
            print(f'{counter2} {counter1}: {image_url} - yet')
            continue
        else:
            print(f'{counter2} {counter1}: {image_url} - yet')
            continue
    image_data = requests.get(image_url).content
    with open(f'wallpapers/{image_name}.jpg', 'wb') as file:
	       file.write(image_data)
    counter1+=1
    print(f'{counter2} {counter1}: {image_url} - uploaded')
