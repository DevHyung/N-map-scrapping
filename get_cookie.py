from selenium import webdriver
import time
from urllib.parse   import quote
def get_url_encode(_query):
    return quote(_query).replace('%20', '+')

def get_cookie_str(_cookie):
    cookieStr = ""
    for cookie in _cookie:
        cookieStr += "{}={};".format(cookie['name'],cookie['value'])
    return  cookieStr

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('https://map.naver.com/')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="search-input"]').send_keys('영통동 음식집\n')
print(get_cookie_str(driver.get_cookies()))
time.sleep(3)
driver.quit()