# Chapter 02 동적 웹페이지 크롤링 하기
# chapter 02-1 실전 크롤링: 다음 뉴스 기사의 댓글 가져오기
# 2019-12-16 20:06

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

chromedriver = './webdriver/chrome/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://news.v.daum.net/v/20191216195402155')

loop, count = True, 0

while loop and count < 10:
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#alex-area > div > div > div > div.cmt_box > div.alex_more > a'))
        )
        more_button = driver.find_element_by_css_selector('#alex-area > div > div > div > div.cmt_box > div.alex_more > a')
        webdriver.ActionChains(driver).click(more_button).perform()
        count += 1
        time.sleep(2)
    except TimeoutException:
        loop = False

driver.quit()