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
driver.get("https://ojt.wda.gov.tw/ClassSearch")

driver.find_element(By.CSS_SELECTOR,'input[id="Form_PlanType_1"]').click()

#以下二選一即可
driver.find_element(By.CSS_SELECTOR,'input[placeholder="請輸入課程名稱"]').send_keys("大數據")
#driver.find_element(By.CSS_SELECTOR,'input[title="請輸入課程名稱檢索"]').send_keys("大數據")

#以下二選一即可
driver.find_element(By.CSS_SELECTOR,'button[class="btn-orange"]').click()
#driver.find_element(By.CSS_SELECTOR,'button[title="送出").click()

#以下二選一即可
#driver.find_element(By.CSS_SELECTOR,'button[class="btn btn-info"]').click()
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
from bs4 import BeautifulSoup

#撈取當頁所有網頁連結
soup = BeautifulSoup(driver.page_source,"html.parser")
#print(soup.find("div",class_="table-responsive"))

#以下二選一即可
#print(soup.find("td",headers="tb1-b").a.text)
#print(soup.find_all("td",style="text-align:left"))

 
    
while soup.find("a",id="nextPage")["class"]!=["disabled"]:
      #fin_all出來為"list格式" 
    for class_name in soup.find_all("td",style="text-align:left"):
        a=class_name.a.text
        print(a)
   #點擊下一頁    
    driver.find_element(By.CSS_SELECTOR,'a[id="nextPage"]').click()
   #新的下一頁網頁    
    soup = BeautifulSoup(driver.page_source,"html.parser")





