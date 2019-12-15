# Chapter 01 브라우저 제어해서 크롤링 하기
# chapter 01-5 브라우저를 제어해서 크롤링 하기 - Headless Chrome과 PhantomJS 익히기
# 2019-12-15 18:21

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
headless_options.add_argument('lang=ko_KR')


driver = webdriver.Chrome(chromedriver, options=headless_options)


driver.get('http://www.python.org')

# Selenium은 웹 테스트를 위한 프레임워크로 다음과 같은 방식으로 웹테스트를 자동으로 진행함
assert "Python" in driver.title

search = driver.find_element_by_name("q")
search.clear()

# 키 이벤트 전송
search.send_keys("python")

# 엔터 입력
search.send_keys(Keys.RETURN)

# 명시적으로 일정 시간을 기다릴 수 있음
time.sleep(2)

assert "No results found." not in driver.page_source

data = driver.find_elements_by_css_selector("#content > div > section > form > ul > li > h3 > a")
for item in data:
    print(item.text)

# 브라우저 종료
driver.quit()