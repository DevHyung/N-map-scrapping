
from bs4 import BeautifulSoup
import json
import time
import requests
import random
from urllib.parse   import quote
from CONFIG import *

def get_url_encode(_query):
    return quote(_query).replace('%20', '+')

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

if __name__ == "__main__":
    # CODE HERE 

