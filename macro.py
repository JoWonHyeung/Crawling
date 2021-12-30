from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import requests
from bs4 import BeautifulSoup

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

#1. 로그인
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
broswer = webdriver.Chrome("C:\\tmp\\chromedriver.exe",options=options)
broswer.get("https://portal.sejong.ac.kr/jsp/login/loginSSL.jsp?rtUrl=sjpt.sejong.ac.kr/main/view/Login/doSsoLogin.do?p=")
time.sleep(1)

input_js = ' \
    document.getElementById("id").value = "{id}"; \
    document.getElementById("password").value = "{pw}"; \
    '.format(id = "19013137", pw = "dnjsgud@12")
broswer.execute_script(input_js)
elem = broswer.find_element_by_id("loginBtn").click()
time.sleep(1)

#2. '주의사항 확인' 클릭
broswer.find_element_by_link_text("확인").click()
time.sleep(3)                                                                                                                              

#3. '수업/성적' 클릭
broswer.find_element_by_id("mf_wfrLeftTreeMenu_treLeftMenu_label_22").click()
time.sleep(3)

#4. '강좌조회 및 수강신청' 클릭
broswer.find_element_by_id("mf_wfrLeftTreeMenu_treLeftMenu_label_23").click()
time.sleep(3)

#5. '수강신청' 클릭
broswer.find_element_by_id("mf_wfrLeftTreeMenu_treLeftMenu_label_27").click()

