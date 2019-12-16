# Chapter 01 브라우저 제어해서 크롤링 하기
# chapter 01-7 실전 크롤링: 브라우저를 제어해서 트위터 사이트 로그인 하기
# 2019-12-16 09:47

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = './webdriver/chrome/chromedriver.exe'
# driver = webdriver.Chrome(chromedriver)

# driver = webdriver.PhantomJS('C:\\phantomjs\\bin\\phantomjs')

headless_options = webdriver.ChromeOptions()
headless_options.add_argument('headless')
headless_options.add_argument('window-size=1920x1080')
headless_options.add_argument('disable-gpu')
headless_options.add_argument("user-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36")
headless_options.add_argument('lang=ko_KR')

driver = webdriver.Chrome(chromedriver, options=headless_options)

driver.get('https://twitter.com/login')
# title = driver.find_element_by_tag_name("h3")
id_field = driver.find_element_by_name("session[username_or_email]")
id_field.clear()
id_field.send_keys("marinehayong")
pw_field = driver.find_element_by_name("session[password]")
pw_field.send_keys("password")
pw_field.send_keys(Keys.RETURN)

time.sleep(2)

data = driver.find_elements_by_css_selector('div.content > div.js-tweet-text-container > p')
for item in data:
    print(item.text)

# 브라우저 종료
driver.quit()