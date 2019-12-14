# Chapter 01 브라우저 제어해서 크롤링 하기
# chapter 01-2 브라우저를 제어해서 크롤링 하기-Selenium 기본 사용법 익히기 1
# 2019-12-14 05:17

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = './webdriver/chrome/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.get('http://www.python.org')

elem = driver.find_element_by_name("q")
elem.clear()

# 키 이벤트 전송
elem.send_keys("python")

# 엔터 입력
elem.send_keys(Keys.RETURN)

# 명시적으로 일정 시간을 기다릴 수 있음
time.sleep(2)

h3s = driver.find_elements_by_tag_name("h3")
for h3 in h3s:
    print(h3.text)

# 브라우저 종료
driver.quit()

