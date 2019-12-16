# Chapter 01 브라우저 제어해서 크롤링 하기
# chapter 01-8 내가 해보는 크롤링 실습(자소설 채팅방 긁어보기)
# 2019-12-16 15:57

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

driver.get('https://jasoseol.com/chat/8964')
# title = driver.find_element_by_tag_name("h3")
datas = driver.find_elements_by_class_name("chat-message-receive")

time.sleep(2)

for data in datas:
    print(data.text)

# 브라우저 종료
driver.quit()

# 흠 위에 스크롤 해서 하는건 아직 모르겠네