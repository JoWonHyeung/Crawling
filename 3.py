from selenium import webdriver
import time

query_text = input("1. 수집할 자료의 키워드는 무엇입니까?")
print("\n")

chrome_path = "C:\\tmp\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = 'http:\\riss.kr'
driver.get(url)
time.sleep(2)

element = driver.find_element_by_name("query")
driver.find_element_by_name("query").click()
element.send_keys(query_text)
element.send_keys("\n")

#학위 논문 선택하기
driver.find_element_by_link_text("학위논문").click()
time.sleep(2)

#본문 내용 추출
from bs4 import BeautifulSoup
html_1 = driver.page_source
soup_1 = BeautifulSoup(html_1, 'html.parser')

content_1 = soup_1.find('div','srchResultListW').find_all('li')


import sys
f_name = input('결과를 저장할 파일명을 쓰세요 : ')

orig_stdout = sys.stdout
file = open(f_name,'a',encoding='UTF-8')
sys.stdout = file

for i in content_1:
    print(i.get_text().replace("\n",""))
    
file.close()
sys.stdout = orig_stdout
    