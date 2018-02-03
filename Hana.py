from selenium import webdriver
from datetime import date
from datetime import datetime
import time
import os
import random
print("_______________________________________________")
print("*** Made By Park HyungJune copyright @ DevHyung")
print(">>> This program semi Auto version ")
print(">>> 하나카드 버전")
f = open("option.txt", 'r', encoding='utf8')
option = f.readlines()
id = option[26].strip()
pw = option[28].strip()
print(">>>ID, PW :: ",id,pw)
def hana():
    try:
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.getcwd() + "\하나"}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chromeOptions)
        driver.maximize_window()
        driver.get('https://www.hanacard.co.kr/OMM05000000C.web?schID=mcd&mID=OMM05000000M')
        time.sleep(5)
        input(">>> 로그인후 엔터를 눌러주세요 ")
        while True:
            print("_" * 30)
            print(">>> 매일 새벽 6:30 분에 자동으로 작동 시작됩니다.")
            print(">>> 작동시작 시간 : ", datetime.now())
            print(">>> 대기중...")
            while True:
                time.sleep(random.randint(57,60))
                curTime = datetime.now()
                if (curTime.hour == 6 and curTime.minute == 30):
                    print(">>> Try Time : ", curTime)
                    print(">>> 보안프로그램 업데이트 또는, 사이트개편으로 실패한것만 아래에 로그가 남습니다.")
                    break

                driver.find_element_by_xpath('//*[@id="gnb"]/div/ul/li[1]/a').click()
            driver.get('https://www.hanacard.co.kr/OMY05000000M.web?schID=mcd&mID=OMY05000000M')
            time.sleep(3)
            today = date.today().strftime("%Y%m%d")
            yesterday = date.fromtimestamp(time.time() - 60 * 60 * 24).strftime("%Y%m%d")
            driver.find_element_by_xpath('//*[@id="form1"]/div/div/div/div/fieldset/ul[1]/li[3]/ul/li[1]/label').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="SLRCP_SDT"]').clear()
            driver.find_element_by_xpath('//*[@id="SLRCP_SDT"]').send_keys(yesterday)
            driver.find_element_by_xpath('//*[@id="SLRCP_EDT"]').clear()
            driver.find_element_by_xpath('//*[@id="SLRCP_EDT"]').send_keys(today)
            driver.find_element_by_xpath('//*[@id="form1"]/div/div/div/div/fieldset/ul[2]/li/a').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="resultArea2"]/div[1]/ul/li[2]/a').click()
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="gnb"]/div/ul/li[1]/a').click()
    except:
        print(">>> 하나 오류")
        driver.save_screenshot(os.getcwd() + "\하나오류.jpg")
        driver.quit()
if __name__=="__main__":
    hana()
    input()
