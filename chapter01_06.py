# Chapter 01 브라우저 제어해서 크롤링 하기
# chapter 01-6 실전 크롤링: 브라우저를 제어해서 다음 뉴스 기사 제목 가져오기
# 2019-12-15 18:33

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

driver.get('http://news.v.daum.net/v/20170202185812986')
# title = driver.find_element_by_tag_name("h3")
title = driver.find_element_by_id('harmonyContainer')
print(title.text)

# 브라우저 종료
driver.quit()