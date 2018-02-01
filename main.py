from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date
import time
import os

print("_______________________________________________")
print("*** Made By Pakr HyungJune copyright @ DevHyung")
f = open("option.txt", 'r', encoding='utf8')
today = date.today().strftime("%Y%m%d")
yesterday = date.fromtimestamp(time.time() - 60*60*24).strftime("%Y%m%d")
option = f.readlines()
samsumgID = option[14].strip()
samsumgPW = option[16].strip()

def samsung(driver):
    driver.get('https://www.samsungcard.com/merchant/login/UHPMCO0103M0.jsp')
    driver.find_element_by_xpath('//*[@id="dgtlMmbrId"]').send_keys(samsumgID)
    driver.find_element_by_xpath('//*[@id="pswde"]').send_keys(samsumgPW)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="butnLgn"]').click()
    time.sleep(3)
    driver.get('https://www.samsungcard.com/merchant/deposit/UHPMRP0301M0.jsp')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="cusomtSelectbox_28_button"]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="cusomtSelectbox_28_menu"]/div[1]/ul/li[5]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="uiInqrStrtdt"]').send_keys(yesterday)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="uiInqrEnddt"]').send_keys(today)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="btnDld"]').click()
if __name__=="__main__":
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": os.getcwd() }
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path="./chromedriver",chrome_options=chromeOptions)
    driver.maximize_window()
    samsung(driver)
