from selenium import webdriver
import time
tmp = [{'domain': '.map.naver.com', 'expiry': 1535306319.033379, 'httpOnly': False, 'name': '_naver_usersession_', 'path': '/', 'secure': False, 'value': 'ie0uIjkaTeukjJ191JbgWg=='}, {'domain': '.map.naver.com', 'expiry': 1535308117.978455, 'httpOnly': False, 'name': 'ASkLHyKNXxrQXUYHKHCxneJLq0', 'path': '/', 'secure': False, 'value': '"H3xITg695nQOk2uWcgcHQeJKciU=|QK5oQy9BL4cmvKO0|1535302800000"'}, {'domain': 'map.naver.com', 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': 'BE2414BBC3357907829C03F975084AF3'}, {'domain': '.naver.com', 'httpOnly': False, 'name': 'page_uid', 'path': '/', 'secure': False, 'value': 'TG7SLwpy72KssakGHthssssssZ4-064112'}, {'domain': '.naver.com', 'expiry': 3113224118.335139, 'httpOnly': False, 'name': 'npic', 'path': '/', 'secure': False, 'value': 'ykO7O2uWgtxv9g3fQTXRibQIHhv+TKkvTLMudIFjFUy6jILPZTPBgAU6rYNVXGYyCA=='}, {'domain': '.naver.com', 'expiry': 2524640399.729149, 'httpOnly': False, 'name': 'NNB', 'path': '/', 'secure': False, 'value': 'SDQBYKRX2WBFW'}]
print(tmp[0])

exit(-1)
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('https://map.naver.com/')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="search-input"]').send_keys('영통동 음식집\n')
print(driver.get_cookies())
time.sleep(3)
driver.quit()