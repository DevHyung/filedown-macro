from selenium import webdriver
from datetime import date
from datetime import datetime
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
print("_______________________________________________")
print("*** Made By Park HyungJune copyright @ DevHyung")
print(">>> 로그인만 테스트 하는 프로그램 ")
print(">>> Include 삼성, 신한, 국민, 롯데, Tpay, Sem ")
print(">>> 아래 실패가 되었다고 나올시에 보안프로그램 업그레이드 또는")
print(">>> 설치를 해주시면 됩니다.")
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
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="dgtlMmbrId"]').send_keys(samsumgID)
        time.sleep(2)
        driver.execute_script("document.getElementById('pswde').value = '" + samsumgPW + "'")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="butnLgn"]').click()
        time.sleep(3)
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
        time.sleep(5)
        driver.execute_script("document.getElementById('memid').value = '"+sinhanID+"'")
        driver.execute_script("document.getElementById('fpass').value = '" + sinhanPW + "'")
        driver.find_element_by_xpath('//*[@id="loginType01"]/div/input').click()
        time.sleep(3)
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
        time.sleep(3)
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
        time.sleep(3)
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
