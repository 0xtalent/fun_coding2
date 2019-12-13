# Chapter 01 브라우저 제어해서 크롤링 하기
# chapter 01-1 브라우저를 제어해서 크롤링 하기-Selenium 이해 및 설치
# 2019-12-13 17:24

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = './webdriver/chrome/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)