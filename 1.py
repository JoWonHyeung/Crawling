#1
from gc import collect
from selenium import webdriver
import time

#2
print("=" * 100)
print("RISS 사이트의 논문 및 학술 자료 수집")
print("=" * 100)
query_txt = input("1.수집할 자료의 키워드는 무엇인가?")

#3
fc_name = input("결과를 저장할 csv형식의 파일명을 쓰세요(예시: c:\\temp\\riss.csv) : ")
fx_name = input("결과를 저장할 txt형식의 파일명을 쓰세요(예시: c:\\temp\\riss.txt) : ")

#4
chrome_path = "C:\\tmp\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = 'http://www.riss.kr/'
driver.get(url)
time.sleep(2)

#5
element = driver.find_element_by_id("query")
driver.find_element_by_id("query").click()
element.send_keys(query_txt)
element.send_keys("\n")
time.sleep(2)

#6
driver.find_element_by_link_text('학위논문').click()
time.sleep(2)

#7
from bs4 import BeautifulSoup
html_1 = driver.page_source
soup_1 = BeautifulSoup(html_1,'html.parser')

content_1 = soup_1.find('div','srchResultListW').find_all('li')
for i in content_1:
    print(i.get_text().replace("\n",""))
print()

#8
import math
total_cnt = soup_1.find('div','searchBox pd').find('span','num').get_text()
print("검색하신 키워드 %s 으로 총 %s 건의 학위논문이 검색되었습니다." %(query_txt,total_cnt))
collect_cnt = int(input('이 중에서 몇 건을 수집하시겠습니까?'))
collect_page_cnt = math.ceil(collect_cnt / 10)
print("%s 건의 데이터를 수집하기 위해 %s 페이지의 게시물을 조회합니다." %(collect_cnt,collect_page_cnt))

#9
page_no = []
no = 1
for i in range(10,collect_cnt):
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
            f = open(fx_name,'a',encoding="UTF-8")
            print("번호:",no)
            f.write("번호:" + str(no) + "\n")
            
            print("제목:",title)
            f.write("제목:" + title + "\n") 
                
            content = b.find('p','preAbstract').get_text()
            print("내용:",content)
            f.write("내용:" + content + "\n")
            f.write("\n")
            print()
            f.close()
            
            no += 1
            
            if no > collect_cnt:
                break        
            time.sleep(2)    
        

c = math.floor(a/10)-1

a += 1

if a == page_no[c]:
    driver.find_element_by_link_text('다음 페이지로').click()
else:
    driver.find_element_by_link_text('%s'%a).click()
