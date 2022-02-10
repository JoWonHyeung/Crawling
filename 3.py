#1
from gc import collect
from operator import index
from selenium import webdriver
from bs4 import BeautifulSoup
import time

#2
print("=" * 100)
print("Naver dataLab 분야 통계 Top500 수집")
print("=" * 100)
print(f"1. 패션의류\t2.패션잡화\t3.화장품/미용\t4.디지털/가전\t5.가구/인테리어\t")
print(f"6. 출산/육아\t7.식품\t8.스포츠/레저\t9.생활/건강\t10.여가/생활편의\t")
number = int((input("1)수집할 자료의 키워드 번호를 입력하세요 :")))
print()
keywords = [
    '패션의류',
    '패션잡화',
    '화장품/미용',
    '디지털/가전',
    '가구/인테리어',
    '출산/육아',
    '식품',
    '스포츠/레저',
    '생활/건강',
    '여가/생활편의'
]
keyword = keywords[number - 1]

#3
fx_name = input("결과를 저장할 txt형식의 파일명을 쓰세요(예시: c:\\temp\\riss.txt) : ")
fc_name = input("결과를 저장할 txt형식의 파일명을 쓰세요(예시: c:\\temp\\riss.csv) : ")
print()

#4
chrome_path = "C:\\tmp\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(chrome_path,options=options)
driver.maximize_window()

url = 'https://datalab.naver.com/shoppingInsight/sCategory.naver'
driver.get(url)
time.sleep(2)

#5 사용자로 부터 건수 입력
import math

print(f"<'{keyword}' 키워드로 크롤링합니다>")
collect_cnt = int(input("이 중에서 크롤링 할 건수는 몇건입니까? "))
collect_page_cnt = math.ceil(collect_cnt / 20)
print(f'{keyword} 키워드로 {collect_cnt}건의 정보를 수집하겠습니다.')
print(f'{collect_page_cnt}페이지를 탐색합니다.')
print()

#5. 분야 선택하기
driver.find_element_by_class_name("select_btn").click()
time.sleep(1)

driver.find_element_by_link_text(keyword).click()
time.sleep(1)

driver.find_element_by_link_text('조회하기').click()
time.sleep(1)

no = 1

num = []
item = []

#6. 인기 검색어 수집
for a in range(1,collect_page_cnt + 1):
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    content = soup.find('ul','rank_top1000_list').find_all('li')
    
    for b in content:
        f = open(fx_name,'a',encoding='UTF-8')
        
        data = b.get_text()
        
        numbers = "0123456789"
        data = ''.join( x for x in data if x not in numbers)
        data.strip()
        
        num.append(no)
        item.append(data)
        f.write(f'{no}. {data}\n')
        print(f'{no}. {data}\n')
        
        f.close()
        
        no += 1
        
        if no > collect_cnt:
            break
        time.sleep(1)
        
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[2]').click()
    time.sleep(1)
    

#7 csv파일 저장
import pandas as pd

df = pd.DataFrame()
df['번호'] = num
df['아이템'] = item

df.to_csv(fc_name,index=False,encoding="utf-8-sig")
print("===수집완료===")