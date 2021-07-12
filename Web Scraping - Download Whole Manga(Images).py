import requests
from bs4 import BeautifulSoup
import os
for x in range(1,158):
    url = 'https://www.mangainn.net/solo-leveling-3/%s/all-pages'%(x)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    path = 'D:\Data Science\Project\Solo Leveling'
    name = 0
    folder_name = soup.title.text
    folder = os.path.join('D:\Data Science\Project\Solo Leveling', folder_name)
    file_name = '{}.txt'.format(folder_name)
    file = os.path.join(folder, file_name)
    os.makedirs(folder)
    os.chdir('D:\Data Science\Project\Solo Leveling\%s'%(folder_name))
    for image in images:
        link = image['src']
        with open(str(name) + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
        name = name + 1
