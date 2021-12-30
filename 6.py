from selenium import webdriver
from bs4 import BeautifulSoup 
import time

query_text = input("수집할 자료의 키워드를 입력하세요 : ")

fc_name = input("결과를 저장할 csv형식의 파일명을 쓰세요 : ")

chrome_path = "C:\\tmp\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(chrome_path,options=options)

url = "http:\\www.riss.kr"
driver.get(url)
time.sleep(2)

element = driver.find_element_by_id("query")
driver.find_element_by_id("query").click()
element.send_keys(query_text)
element.send_keys("\n")

#학위 논문 클릭
time.sleep(2)
driver.find_element_by_link_text("학위논문").click()

html_1 = driver.page_source
soup_1 = BeautifulSoup(html_1,'html.parser')

#총 검색 건수를 보여주고 수집할 건수 입력받기
import math
total_cnt = soup_1.find('div','searchBox pd').find('span','num').get_text()
print("'%s'키워드로 검색된 학위논문의 개수는 %s건 입니다" %(query_text,total_cnt))
collect_cnt = int(input("수집할 건수를 입력하세요 : "))
collect_page_cnt = math.ceil(collect_cnt / 10)
print("%s건의 데이터를 수집하기 위해 %s페이지의 게시물을 조회합니다" %(collect_cnt,collect_page_cnt))

no = 1
page_no =[]

for i in range(10, collect_cnt) :
    if i % 10 == 0:
        page_no.append(i + 1)

for a in range(1, collect_page_cnt + 1):
    html_2 = driver.page_source
    soup_2 = BeautifulSoup(html_2,'html.parser')
    
    content_2 = soup_2.find('div','srchResultListW').find_all('li')
    
    for b in content_2:
        try:
            title = b.find('div','cont').find('p','title').get_text()
        except:
            continue
        else:
            print('번호 : ',no)
            
            print('논문제목 : ',title) 
            
            writer = b.find('div','cont').find('span','writer').get_text()
            print('저자 : ', writer)

            org = b.find('div','cont').find('span','assigned').get_text()
            print('소속기관 : ', org) 
            
            no+=1
            print("\n")
        
            if no > collect_cnt :
                break
            time.sleep(1)
    
    c = math.floor(a/10)-1    
    a += 1
    
    if a == page_no[c]:
        driver.find_elements_by_link_text('다음 페이지로').click()
    else :
        driver.find_element_by_link_text('%s' %a).click()
    
    
        
               
    