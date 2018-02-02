from selenium import webdriver
from datetime import date
from datetime import datetime
import time
import os
import random
print("_______________________________________________")
print("*** Made By Park HyungJune copyright @ DevHyung")
print(">>> This program semi Auto version ")
print(">>> 현대카드 버전")
f = open("option.txt", 'r', encoding='utf8')
option = f.readlines()
id = option[2].strip()
pw = option[4].strip()
print(">>>ID, PW :: ",id,pw)
def hyundae():
    try:
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.getcwd() + "\현대"}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chromeOptions)
        driver.maximize_window()
        driver.get('https://www.hyundaicard.com/csa/mb/STOREMAIN.hc')
        time.sleep(5)
        input(">>> 로그인후 엔터를 눌주세요")
        while True:
            print("_"*30)
            print(">>> 매일 새벽 6:20 분에 자동으로 작동 시작됩니다.")
            print(">>> 작동시작 시간 : ", datetime.now())
            print(">>> 대기중...")
            while True:
                # if your start 6:20  below start 6:21
                curTime = datetime.now()
                if (curTime.hour == 6 and curTime.minute == 20) or (curTime.hour == 6 and curTime.minute == 21):
                    print(">>> Try Time : ", curTime)
                    print(">>> 보안프로그램 업데이트 또는, 사이트개편으로 실패한것만 아래에 로그가 남습니다.")
                    break
                time.sleep(random.randint(58,62))
                driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/h1/a').click()
            time.sleep(1)
            today = date.today().strftime("%Y%m%d")
            yesterday = date.fromtimestamp(time.time() - 60 * 60 * 24).strftime("%Y%m%d")
            driver.find_element_by_xpath('//*[@id="container"]/div[1]/ul/ul[1]/li[4]/dl/dd/ul/li[1]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="iqryPrd1"]').clear()
            driver.find_element_by_xpath('//*[@id="iqryPrd1"]').send_keys(yesterday)
            driver.find_element_by_xpath('//*[@id="iqryPrd2"]').clear()
            driver.find_element_by_xpath('//*[@id="iqryPrd2"]').send_keys(today)
            driver.find_element_by_xpath('//*[@id="searchBtn1"]').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="excelBtn1"]').click()
            time.sleep(10)
            driver.get('https://www.hyundaicard.com/csa/mb/STOREMAIN.hc')
    except:
        print(">>> 현대 오류")
        driver.save_screenshot(os.getcwd()+"\현대오류.jpg")
        driver.quit()
if __name__=="__main__":
    hyundae()
    input()
