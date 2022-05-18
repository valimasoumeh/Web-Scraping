import scrapy
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

import time

drive_path = r"C:\Users\Masoumeh\Desktop\chromedriver_win32\Chromedriver.exe"

# Chrome Option
option = webdriver.ChromeOptions()

lst = []
driver = webdriver.Chrome(drive_path, chrome_options=option)
driver.get("https://www.varzesh3.com/")
what_search_box = driver.find_element_by_name("searchKey")
what_search_box.send_keys("مسی")
what_search_box.send_keys(Keys.ENTER)
# # titles=driver.find_element_by_xpath("//*[@id="anc"]/div[3]/ul/li[1]/div[2]/h3/a").get_
# titles=(driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[3]/ul/li[21]/div[2]/h3/span").text)
# lst.append(titles)
# print(lst)


# max_date = datetime.strptime('2018-01-01', '%Y-%m-%d')


# try:/
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


# time.sleep(2)
# more=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[3]/button")
# except:
# more.click()
# time.sleep(10)
# driver.close()
# time.sleep(5)

#
# more_key=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/button')
# more_key.send_keys(Keys.ENTER)
i = 1
lst = []
col = ["date", "text", "summary"]
date_list=[]
text_list=[]
summary_list=[]

while True:

    try:
        dates = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div[3]/ul/li[" + str(i) + "]/div[2]/h3/span").text
        texts = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div[3]/ul/li[" + str(i) + "]/div[2]/h3/a").text
        summarys = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div[3]/ul/li[" + str(i) + "]/div[2]/p").text
        date_list.append(dates)
        text_list.append(texts)
        summary_list.append(summarys)
        ziped=zip(date_list,text_list,summary_list)



        i += 1
    except NoSuchElementException:

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        more = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[3]/button")
        more.click()

    if dates == "هفته پیش":
        break
lst=list(ziped)
print(lst)

df = pd.DataFrame(lst, columns=col)
df.to_csv("out.csv",encoding="utf-8")

driver.close()

