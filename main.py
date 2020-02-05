#import requests
#from bs4 import BeautifulSoup

#page = requests.get('https://www.instagram.com/paollaolsen/')
#soup = BeautifulSoup(page.text, 'html.parser')

# artist_name_list = soup.find(class_='BodyText')
# artist_name_list_items = artist_name_list.find_all('a')

# print(soup)

#item = soup.find('div', {'class':'v1Nh3 kIKUG  _bz0w'})

#print(item)

#link = item.find_all('a')

#print(link)

from selenium import webdriver

import time
import numpy as np

browser = webdriver.Firefox()
browser.implicitly_wait(10)

browser.get('https://www.instagram.com/')

ifLogged = len(browser.find_elements_by_css_selector('._2dbep.qNELH.kIKUG'))
print(ifLogged)

while ifLogged == 0:
   print('Not exists')
   ifLogged = len(browser.find_elements_by_css_selector('._2dbep.qNELH.kIKUG'))
   # print(ifLogged)

browser.get('https://www.instagram.com/paollaolsen/')
browser.implicitly_wait(10)

# quantityPosts = int(browser.find_element_by_css_selector('.g47SY').text)
# print(quantityPosts)

# quantityPostsAtual = 0

content = browser.find_elements_by_css_selector('.v1Nh3 a')

SCROLL_PAUSE_TIME = 0.5

last_height = browser.execute_script("return document.body.scrollHeight")

photos = []

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = browser.execute_script("return document.body.scrollHeight")
    content = browser.find_elements_by_css_selector('.v1Nh3 a')
    for item in content:   
        browser.execute_script("arguments[0].click();", item)
        if browser.find_elements_by_css_selector('.PdwC2 .FFVAD'):
            photo = browser.find_element_by_css_selector('.PdwC2 .FFVAD')
            link = photo.get_attribute("src")
            photos.append(link)
        if browser.find_elements_by_css_selector('.PdwC2 .tWeCl'):
            video = browser.find_element_by_css_selector('.PdwC2 .tWeCl')
            link = video.get_attribute("src")
            photos.append(link)
    # print(photos)
    # print('***')
    if new_height == last_height:
        break
    last_height = new_height

photos = np.unique(photos)

#print(photos)
print(len(photos))