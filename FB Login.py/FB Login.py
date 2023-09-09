from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

services=Service(executable_path="C:\\Users\\user\\Desktop\\chromedriver.exe")
driver=webdriver.Chrome(service=services)
driver.get("https://www.facebook.com")

driver.find_element(By.CSS_SELECTOR,'input[name="email"]').send_keys("************@yahoo.com.tw")
driver.find_element(By.CSS_SELECTOR,'input[name="pass"]').send_keys("***********")
driver.find_element(By.CSS_SELECTOR,'button[name="login"]').click()


