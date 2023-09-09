#google重頭開始搜尋到載入
#開一個資料夾
import os
#path=os.getcwd()
#存在桌面
#path=os.path.join("C:\\Users\\User\\Desktop\\海賊王")
path=os.path.join("海賊王")
#os.mkdir(path)



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
driver.get("https://www.google.com.tw/?hl=zh_TW")

driver.find_element(By.CSS_SELECTOR,'textarea[jsname="yZiJbe"]').send_keys("海賊王")
driver.find_element(By.CSS_SELECTOR,'textarea[jsname="yZiJbe"]').send_keys(Keys.ENTER)

#以下二選一
#driver.find_element(By.XPATH,(//*[@id="bqHHPb"]/div/div/div[1]/a[1]/div/span)
driver.find_element(By.XPATH,('//*[text()="圖片"]')).click()

driver.find_element(By.CSS_SELECTOR,'div[jsname="I4bIT"]').click()
driver.find_element(By.XPATH,('//*[text()="大小"]')).click()
driver.find_element(By.XPATH,('//*[text()="圖示"]')).click()

#下載圖片連結
pics=driver.find_elements(By.CSS_SELECTOR,'a[class="wXeWr islib nfEiy"]')
picws=[]
for pic in pics:
    pic.click()
    picws.append(pic.get_attribute("href"))
#print(picws)

#from time import sleep
imgs=[]
for url in picws[:10]:
    #無法讀取的特別列出
    try:
        driver.get(url)
        #sleep(10)
        #定位目標by.css_selector完，取得屬性src
        imgs.append(driver.find_element(By.CSS_SELECTOR,'img[class="r48jcc pT0Scc iPVvYb"]').get_attribute("src"))
    except:
        print(url)
print(imgs)


#圖片儲存至資料夾
import wget
n=1
for img in imgs:
    try:
        #file=os.path.join(path,"海賊王"+str(n)+".jpg")
        file=os.path.join("海賊王","海賊王"+str(n)+".jpg")
        wget.download(img,file)
        n+=1
    except:
        print(img)

        