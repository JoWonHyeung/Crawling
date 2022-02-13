import unicodedata
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime

### Scroll_down 함수! 매우 중요
def scroll_down(browser):
    broswer.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)


#1 정보 입력
print("="*100)
print("인스타그램의 해시태그 정보 수집")
print("="*100)

id = input("1.Instagram의 Id를 입력하세요: ")
passwd = input("2.Instagram의 passwd를 입력하세요: ")
query_txt = input("3. 검색할 해쉬태그를 입력하세요(ex:강남맛집): ")
cnt = int(input("크롤링 할 건수는 몇건입니까? "))

f_dir = input("파일이 저장될 경로를 쓰세요(ex:C://tmp//) : ")

now = datetime.datetime.now()

fx_name = f_dir + f'Instagram-{query_txt}-{now.year}-{now.month:02}-{now.day:02}' + '.txt'
fc_name = f_dir + f'Instagram-{query_txt}-{now.year}-{now.month:02}-{now.day:02}' + '.csv'

#2 driver 실행
chrome_path = "C:\\tmp\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
broswer = webdriver.Chrome(chrome_path,options=options)
broswer.get("https://www.instagram.com/accounts/login/")
time.sleep(1)

#3 ID, PWD 입력
eid = broswer.find_element_by_name('username')
for a in id:
    eid.send_keys(a)
    time.sleep(0.3)
    
epwd = broswer.find_element_by_name('password')
for b in passwd:
    epwd.send_keys(b)
    time.sleep(0.3)
    
broswer.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()
time.sleep(5)

broswer.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
time.sleep(5)

broswer.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
time.sleep(5)

#4 Query 입력
element = broswer.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
for c in query_txt:
    element.send_keys(c)
    time.sleep(0.2)

time.sleep(2)
broswer.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()

i = 1
while i <= cnt:
    scroll_down(broswer)
    i += 1

#5 URL 수집
item = []
count = 0

html = broswer.page_source
soup = BeautifulSoup(html, 'html.parser')

all = soup.find('article','KC1QD').find_all('a')

for i in all:
    url = i['href']
    item.append('https:\\www.instagram.com' + url)
    count += 1
    
    if count == cnt:
        break

#6 수집한 URL을 활용해서 해시태크 수집
import sys
bmp_map = dict.fromkeys(range(0x10000,sys.maxunicode + 1), 0xfffd)
hash_txt = []
count = 0

for c in range(0, len(item)):
    broswer.get(item[c])
    time.sleep(2)
    
    html = broswer.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    f = open(fx_name,'a',encoding='UTF-8')
    
    tags = soup.find('div','EtaWk')
    
    try:
        tags_1 = tags.find_all('a')
    except:
        pass
    else:
        for d in range(0, len(tags_1)):
            tags = tags_1[d].get_text()
            tags_11 = tags.translate(bmp_map)
            tags_2 = unicodedata.normalize('NFC',tags_11)
            
            for i in tags_2:
                if i[0:1] == '#':
                    hash_txt.append(tags_2)
                    print(tags_2)
                    f.write("\n" + str(tags_2))
    
    f.close()
    
    
#7 csv파일 저장
import pandas as pd
from pandas import DataFrame

df = pd.DataFrame()
df['HashTag'] = hash_txt

df.to_csv(fc_name,index=False,encoding="utf-8-sig")
print("===수집완료===")    
