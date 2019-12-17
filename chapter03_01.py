# Chapter 03 데이터를 선택하는 또 다른 기법: XPATH
# chapter 03-1 실전 크롤링: XPATH와 Selenium 활용해서 페이스북 로그인 하기
# 2019-12-17 13:38

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = './webdriver/chrome/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://wwww.facebook.com/')

user_name = "로그인 아이디"
password = "비밀번호"

# 쉽네 눈으로만 공부합니다
# XPATH가 뭔지만 익숙해지면 됩니다