import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


def test_login():
    driver.get('https://sitweb.22889.club/#/login')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div/div[1]/div[2]/input').send_keys('1770000001')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div/div[2]/div[2]/input').send_keys('123456')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div/div[4]/button').click()
    print('登录成功')
