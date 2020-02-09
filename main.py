from selenium import webdriver

import time
import numpy as np
import requests
import urllib.request

browser = webdriver.Firefox()
browser.implicitly_wait(10)

browser.get('https://www.instagram.com/')

ifLogged = len(browser.find_elements_by_css_selector('._2dbep.qNELH.kIKUG'))
print(ifLogged)

while ifLogged == 0:
   print('Not exists')
   ifLogged = len(browser.find_elements_by_css_selector('._2dbep.qNELH.kIKUG'))

browser.get('https://www.instagram.com/paollaolsen/')
browser.implicitly_wait(10)

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
        if browser.find_elements_by_css_selector('.PdwC2 .tWeCl'):
            photo = browser.find_element_by_css_selector('.PdwC2 .tWeCl')
        link = photo.get_attribute("src")
        photos.append(str(link))
    if new_height == last_height:
        break
    last_height = new_height

photos = np.unique(photos)

print(len(photos))

np.savetxt("data.txt", photos, fmt="%s")

f = open("data.txt","r")
if f.mode == "r":
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        urllib.request.urlretrieve(line, str(i) + '.png')
        print(i)

f.close()