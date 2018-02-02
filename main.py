from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

print("_______________________________________________")
print("*** Made By Park HyungJune copyright @ DevHyung")
f = open("option.txt", 'r', encoding='utf8')
today = date.today().strftime("%Y%m%d")
yesterday = date.fromtimestamp(time.time() - 60*60*24).strftime("%Y%m%d")
option = f.readlines()
sinhanID = option[8].strip()
sinhanPW = option[10].strip()
samsumgID = option[14].strip()
samsumgPW = option[16].strip()
lotteID = option[20].strip()
lottePW = option[22].strip()
hanaID = option[26].strip()
hanaPW = option[28].strip()
kbID = option[32].strip()
kbPW = option[34].strip()
bcID = option[44].strip()
bcPW = option[46].strip()
hdID = option[2].strip()
hdPW = option[4].strip()
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": os.getcwd() }
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path="./chromedriver",chrome_options=chromeOptions)
driver.maximize_window()

def samsung():
    driver.get('https://www.samsungcard.com/merchant/login/UHPMCO0103M0.jsp')
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="dgtlMmbrId"]').send_keys(samsumgID)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="pswde"]').send_keys(samsumgPW)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="butnLgn"]').click()
    time.sleep(2)
    driver.get('https://www.samsungcard.com/merchant/deposit/UHPMRP0301M0.jsp')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="cusomtSelectbox_28_button"]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="cusomtSelectbox_28_menu"]/div[1]/ul/li[5]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="uiInqrStrtdt"]').send_keys(yesterday)
    driver.find_element_by_xpath('//*[@id="uiInqrEnddt"]').send_keys(today)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="btnDld"]').click()
    time.sleep(10)
def sinhan():
    driver.get('https://www.shinhancard.com/cmm/mintg/CMMServiceMemLoginC.shc?mode=initLoginJoin')
    time.sleep(5)
    try:
        driver.implicitly_wait(10)
    except:
        print("오류남")
    driver.execute_script("document.getElementById('memid').value = '"+sinhanID+"'")
    driver.execute_script("document.getElementById('fpass').value = '" + sinhanPW + "'")
    driver.find_element_by_xpath('//*[@id="loginType01"]/div/input').click()
    time.sleep(3)
    driver.get('https://www.shinhancard.com/hpe/HPETRSLTN/prcPmtLt.shc')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ttype_2"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="SDate"]').send_keys(yesterday)
    driver.find_element_by_xpath('//*[@id="EDate"]').send_keys(today)
    time.sleep(3)
    driver.find_element_by_class_name('btnPerformGray').click()
    time.sleep(10)
    driver.find_element_by_class_name('btnArrow').click()
    time.sleep(10)
def hana():

    driver.get('https://www.hanacard.co.kr/OMM05000000C.web?schID=mcd&mID=OMM05000000M')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="USER_ID"]').click()
    driver.find_element_by_xpath('//*[@id="USER_ID"]').clear()
    driver.find_element_by_xpath('//*[@id="USER_ID"]').send_keys(hanaID)
    time.sleep(2)
    input(">>> 로그인후 엔터를 눌러주세요 ")
    #driver.execute_script("document.getElementById('PASSWORD').setAttribute('e2e_type','2');")
    #'document.getElementById('PASSWORD').value ="mall28!!"'
    #driver.execute_script("document.getElementById('PASSWORD').value = '"+hanaPW+"'")
    #driver.find_element_by_xpath('//*[@id="form1"]/div/div/div/article[1]/div/div[1]/fieldset/ul[2]/li[3]/a').click()
    #time.sleep(10)
    driver.get('https://www.hanacard.co.kr/OMY05000000M.web?schID=mcd&mID=OMY05000000M')
    time.sleep(3)
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
def nh():
    driver.get('https://ibz.nonghyup.com/servlet/content/cd/cv/ICBC0002M.thtml')
    time.sleep(5)
    driver.execute_script("goLogin('ICCV')")
def kb():
    driver.get('https://biz.kbcard.com/CXERFZZC0001.cms')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="loginLinkBtn"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="가맹점인터넷서비스로그인ID"]').send_keys(kbID)
    time.sleep(1)
    driver.execute_script("document.getElementById('loginPwdPcr').setAttribute('e2e_type','0');")
    driver.execute_script("document.getElementById('loginPwdPcr').value = '"+kbPW+"'")
    driver.find_element_by_xpath('//*[@id="loginPwdPcr"]').send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="main_contents"]/div/div[1]/div[3]/ul[1]/li[1]/a').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="조회시작년월일"]').clear()
    driver.find_element_by_xpath('//*[@id="조회시작년월일"]').send_keys(yesterday)
    driver.find_element_by_xpath('//*[@id="조회종료년월일"]').clear()
    driver.find_element_by_xpath('//*[@id="조회종료년월일"]').send_keys(today)
    driver.find_element_by_xpath('//*[@id="form1"]/div[1]/div/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="th1_b1"]/a').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="pop_layer"]/div[1]/div[1]/div[1]/div').click()
    time.sleep(3)
    main_window_handle = None
    while not main_window_handle:
        main_window_handle = driver.current_window_handle
    signin_window_handle = None
    while not signin_window_handle:
        for handle in driver.window_handles:
            if handle != main_window_handle:
                signin_window_handle = handle
                break
    driver.switch_to.window(signin_window_handle)
    driver.find_element_by_class_name('report_menu_excel_button_svg').click()
    time.sleep(10)
    driver.close()
    driver.switch_to.window(main_window_handle)  # or driver.switch_to_default_content()
    driver.find_element_by_xpath('//*[@id="pop_layer"]/div[1]/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="th2_b1"]/a').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="pop_layer"]/div[1]/div[1]/div[1]/div').click()
    time.sleep(3)
    main_window_handle = None
    while not main_window_handle:
        main_window_handle = driver.current_window_handle
    signin_window_handle = None
    while not signin_window_handle:
        for handle in driver.window_handles:
            if handle != main_window_handle:
                signin_window_handle = handle
                break
    driver.switch_to.window(signin_window_handle)
    driver.find_element_by_class_name('report_menu_excel_button_svg').click()
    time.sleep(10)
    driver.close()
    driver.switch_to.window(main_window_handle)  # or driver.switch_to_default_content()
    time.sleep(10)

def bc():
    driver2 = webdriver.Ie('./IEDriverServer')
    driver2.get('http://partners.bccard.com/')
    time.sleep(2)
    Alert(driver2).dismiss()
    time.sleep(5)
    driver2.switch_to.frame(driver2.find_element_by_name('mainframe'))
    driver2.find_element_by_xpath('//*[@id="gnbMenu2015"]/ul/li[2]/a').click()
    time.sleep(3)
    driver2.switch_to.frame(driver2.find_element_by_name('incframe'))
    driver2.find_element_by_xpath('//*[@id="id"]').clear()
    driver2.find_element_by_xpath('//*[@id="id"]').send_keys(bcID)
    time.sleep(1)
    driver2.find_element_by_xpath('//*[@id="passwd"]').clear()
    driver2.find_element_by_xpath('//*[@id="passwd"]').send_keys(bcPW + Keys.ENTER)
    time.sleep(10)
def lotte():
    driver.get('https://merchant.lottecard.co.kr/app/index.jsp?1516325676359')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ulGnbMenu"]/li/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ulGnbMenu"]/li[1]/ul/li[3]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="lgn_id"]').send_keys(lotteID)
    time.sleep(1)
    driver.execute_script("document.getElementById('mbr_pswd').setAttribute('e2e_type','0');")
    driver.execute_script("document.getElementById('mbr_pswd').value = '" + lottePW + "'")
    driver.find_element_by_xpath('//*[@id="mbr_pswd"]').send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="sch_start_dt"]').clear()
    driver.find_element_by_xpath('//*[@id="sch_start_dt"]').send_keys(yesterday)
    driver.find_element_by_xpath('//*[@id="sch_end_dt"]').clear()
    driver.find_element_by_xpath('//*[@id="sch_end_dt"]').send_keys(today)
    driver.find_element_by_xpath('//*[@id="searchVO"]/div[1]/div/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="divList"]/div[4]/table/tbody/tr/td[3]/a').click()
    time.sleep(1)
    Alert(driver).accept()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="divList"]/div[1]/ul/li[1]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="divList"]/div[3]/div[1]/a').click()
    time.sleep(3)
    #2번째
    driver.find_element_by_xpath('//*[@id="divList"]/div[4]/table/tbody/tr[2]/td[3]/a').click()
    time.sleep(1)
    Alert(driver).accept()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="divList"]/div[1]/ul/li[1]/a').click()
    time.sleep(10)
    pass
def hyungdae():
    driver.get('https://www.hyundaicard.com/csa/mb/CSAMB0101_01.hc')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="userid"]').send_keys(hdID)
    time.sleep(1)
    #driver.execute_script("document.getElementById('mbr_pswd').setAttribute('e2e_type','0');")
    #driver.execute_script("document.getElementById('mbr_pswd').value = '" + lottePW + "'")
    driver.find_element_by_xpath('//*[@id="userpswd"]').send_keys(hdPW+Keys.RETURN)

if __name__=="__main__":
    #samsung()#성공
    #sinhan()#성공
    #kb() #성공
    #lotte()#성공
    hyungdae()
    #bc() #꼮익스를 써야함
    #hana()  # 이것도 조금 특별히 로그인을 해야한다.
    #nh() # 이것도 로그인하고 해야할듯
    driver.quit()