from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values":{"notification":2}} 
option.add_experimental_option("prefs",prefs)

services=Service(executable_path="C:\\Users\\User\\Desktop\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=services)
driver.get("https://goodinfo.tw/tw2/StockList.asp?SHEET=%E8%82%A1%E5%88%A9%E6%94%BF%E7%AD%96&MARKET_CAT=%E7%86%B1%E9%96%80%E6%8E%92%E8%A1%8C&INDUSTRY_CAT=%E5%90%88%E8%A8%88%E6%AE%96%E5%88%A9%E7%8E%87")

driver.find_element(By.CSS_SELECTOR,'input[id="txtStockCode"]').send_keys("2204")
driver.find_element(By.CSS_SELECTOR,'input[id="btnStockSearch"]').click()
driver.find_element(By.CSS_SELECTOR,'a[href="ShowBuySaleChart.asp?STOCK_ID=2204&CHT_CAT=DATE"]').click()

#webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#driver.find_element(By.CSS_SELECTOR,'span[class_="ns-y13y5-e-16"]').click()


