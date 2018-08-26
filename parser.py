

import json
import requests
from selenium import webdriver
from urllib.parse   import quote
from CONFIG import *
from bs4 import BeautifulSoup
import time
import random


def get_url_encode(_query):
    return quote(_query).replace('%20', '+')

def get_cookie():
    driver.find_element_by_xpath('//*[@id="search-input"]').clear()
    driver.find_element_by_xpath('//*[@id="search-input"]').send_keys(keyword + '\n')
    time.sleep(2)
    # header setting
    return get_cookie_str(driver.get_cookies())

def get_cookie_str(_cookie):
    cookieStr = ""
    for cookie in _cookie:
        cookieStr += "{}={};".format(cookie['name'],cookie['value'])
    return  cookieStr

def get_info():
    html = requests.get(url.format(get_url_encode('합강리 음식집'), 1), headers=headers)
    jsonStr = json.loads(html.text)
    results = jsonStr['result']['site']['list']
    if len(results) != 0:
        for result in results:
            name = result['name']
            address = result['address']
            roadAddress = result['roadAddress']
            tel = result['tel']
            code = result['id'][1:]
            homepage = result['homePage']
            print([name, roadAddress, address, tel, homepage, detailBaseUrl + code])
    else:
        print("끝")
def log(tag, text):
	# Info tag
	if(tag == 'i'):
		print("[INFO] " + text)
	# Error tag
	elif(tag == 'e'):
		print("[ERROR] " + text)
	# Success tag
	elif(tag == 's'):
		print("[SUCCESS] " + text)

if __name__ == "__main__":
    # CODE HERE
    # driver setting
    driver = webdriver.Chrome('./chromedriver')
    driver.maximize_window()
    driver.get('https://map.naver.com/')
    # get cookie
    keyword = input(">>> 검색하실 키워드를 입력 : ").strip()
    headers['cookie'] = get_cookie()

    # get total cnt
    bs4 = BeautifulSoup(driver.page_source,'lxml')
    totalCnt = bs4.find('span',class_='n').em.get_text().strip()
    log('i',"총 {}개 검색결과 존재".format(totalCnt))

    # Parsing 
    time.sleep(3)
    driver.quit()

