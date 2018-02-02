from selenium import webdriver
from datetime import date
from datetime import datetime
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
print("_______________________________________________")
print("*** Made By Park HyungJune copyright @ DevHyung")
print(">>> This program complete Auto version ")
print(">>> Include 삼성, 신한, 국민, 롯데, Tpay, Sem ")
print(">>> 매일 새벽 6:00 분에 자동으로 작동 시작됩니다.")
print(">>> 작동시작 시간 : ", datetime.now())
print(">>> 대기중...")
while True:
    # if your start 6:00  below start 5:59
    curTime = datetime.now()
    if (curTime.hour == 6 and curTime.minute == 1) or (curTime.hour == 6 and curTime.minute == 0):
        print(">>> Try Time : ", curTime)
        print(">>> 보안프로그램 업데이트 또는, 사이트개편으로 실패한것만 아래에 로그가 남습니다.")
        break
    time.sleep(60)
# option Start
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
kbID = option[32].strip()
kbPW = option[34].strip()
tID = option[50].strip()
tPW = option[52].strip()
semID = option[56].strip()
semPW = option[58].strip()
# option End
def samsung():
    try:
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.getcwd()+"\삼성"}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chromeOptions)
        driver.maximize_window()
        driver.get('https://www.samsungcard.com/merchant/login/UHPMCO0103M0.jsp')
        driver.implicitly_wait(10)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="dgtlMmbrId"]').send_keys(samsumgID)
        time.sleep(2)
        driver.execute_script("document.getElementById('pswde').value = '" + samsumgPW + "'")
        # driver.find_element_by_xpath('//*[@id="pswde"]').send_keys(samsumgPW)
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
        driver.quit()
    except:
        print("\t>>>삼성 실패")
        driver.quit()
def sinhan():
    try:
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.getcwd() + "\신한"}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chromeOptions)
        driver.maximize_window()
        driver.get('https://www.shinhancard.com/cmm/mintg/CMMServiceMemLoginC.shc?mode=initLoginJoin')
        time.sleep(10)
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
        driver.quit()
    except:
        print("\t>>>신한 실패")
        driver.quit()
def kb():
    try:
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.getcwd() + "\국민"}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chromeOptions)
        driver.maximize_window()
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
        driver.quit()
    except:
        print("\t>>>국민 실패")
        driver.quit()
def lotte():
    try:
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.getcwd() + "\롯데"}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chromeOptions)
        driver.maximize_window()
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
        driver.quit()
    except:
        print("\t>>>롯데 실패")
        driver.quit()
def tpay():
    try:
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.getcwd() + "\Tpay"}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chromeOptions)
        driver.maximize_window()
        driver.get('https://jms.jtnet.co.kr/jsp/main.jsp')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="userCd"]').send_keys(tID)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(tPW)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="signBtn"]').click()
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//*[@id="bread_AX_basicDialog0_AX_buttons_AX_0"]').click()
        except:
            pass
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ax-top-menu_PMA_1"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ax-top-menu_PMA_1_0"]').click()
        time.sleep(5)
        iframe = driver.find_elements_by_tag_name('iframe')[1]
        driver.switch_to_frame(iframe)
        driver.find_element_by_xpath('//*[@id="tranStart"]').clear()
        driver.find_element_by_xpath('//*[@id="tranStart"]').send_keys(yesterday)
        driver.find_element_by_xpath('//*[@id="tranEnd"]').clear()
        driver.find_element_by_xpath('//*[@id="tranEnd"]').send_keys(today)
        driver.find_element_by_xpath('//*[@id="ax-page-btn-search"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ax-page-btn-excel"]').click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.find_element_by_xpath('//*[@id="ax-top-menu_PMA_1"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ax-top-menu_PMA_1_4"]').click()
        time.sleep(5)
        iframe = driver.find_elements_by_tag_name('iframe')[2]
        driver.switch_to_frame(iframe)
        driver.find_element_by_xpath('//*[@id="tranStart"]').clear()
        driver.find_element_by_xpath('//*[@id="tranStart"]').send_keys(yesterday)
        driver.find_element_by_xpath('//*[@id="tranEnd"]').clear()
        driver.find_element_by_xpath('//*[@id="tranEnd"]').send_keys(today)
        driver.find_element_by_xpath('//*[@id="ax-page-btn-search"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ax-page-btn-excel"]').click()
        time.sleep(10)
        driver.quit()
    except:
        print("\t>>>tpay 실패")
        driver.quit()
def sem():
    try:
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.getcwd() + "\sem"}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chromeOptions)
        driver.maximize_window()
        driver.get('https://semplus.kisvan.co.kr/')
        time.sleep(5)
        frame = driver.find_element_by_tag_name('frame')
        driver.switch_to_frame(frame)
        driver.find_element_by_xpath('//*[@id="ibx_userId"]').send_keys(semID)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ibx_Password"]').send_keys(semPW)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="grp_login"]').click()
        time.sleep(5)

        driver.find_element_by_xpath('//*[@id="generator1_0_btn_TopMenu1"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="generator1_0_generator2_1_btn_TopMenuSub"]').click()
        time.sleep(5)

        iframe = driver.find_element_by_id('windowContainer1_subWindow0_iframe')
        driver.switch_to_frame(iframe)
        driver.find_element_by_xpath('//*[@id="btn_Search"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="grd_Master_cell_0_7"]/nobr').click()
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
        driver.find_element_by_xpath('//*[@id="btn_Excel"]').click()
        time.sleep(10)
        driver.quit()
    except:
        print("\t>>>Sem 실패")
        driver.quit()
if __name__=="__main__":
    samsung()
    sinhan()
    kb()
    lotte()
    tpay()
    sem()
    input()
