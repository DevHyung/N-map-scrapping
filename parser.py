import json
import requests
from selenium import webdriver
from urllib.parse   import quote
from CONFIG import *
from bs4 import BeautifulSoup
import time
import random
from math import ceil


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
    for pageIdx in range(1,lastPage+1):
        log('s',"{} 페이지 추출중...".format(pageIdx))
        html = requests.get(url.format(get_url_encode(keyword), pageIdx), headers=headers)
        jsonStr = json.loads(html.text)
        try:
            results = jsonStr['result']['site']['list']
        except:
            log('e', '쿠키 유효기간 만기로 재갱신중')
            headers['cookie'] = get_cookie()
            log('s', "{} 페이지 추출중...".format(pageIdx))
            html = requests.get(url.format(get_url_encode(keyword), pageIdx), headers=headers)
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
                print(name)
                #print([name, roadAddress, address, tel, homepage, detailBaseUrl + code])
        else:
            log('s',"끝")
        time.sleep(random.randint(3,7))

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
    while True:
        keyword = input(">>> 검색하실 키워드를 입력(끝내려면 'quit' 입력) : ").strip()
        if keyword == 'quit':
            break
        headers['cookie'] = get_cookie()
        headers['cookie'] = 'asd'

        # get total cnt
        bs4 = BeautifulSoup(driver.page_source,'lxml')
        totalCnt = int ( bs4.find('span',class_='n').em.get_text().strip().replace(',','') )
        lastPage = ceil(totalCnt/10)

        log('i',"총 {}개 검색결과 존재".format(totalCnt))
        log('i',"마지막 페이지 {}".format(lastPage))

        # parsing
        get_info()

        # End
    driver.quit()

