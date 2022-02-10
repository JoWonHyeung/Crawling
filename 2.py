from gc import collect
from selenium import webdriver
import time

print("=" * 100)
print("RISS 사이트의 논문 및 학술 자료 수집")
print("=" * 100)
query_txt = input("1.수집할 자료의 키워드는 무엇인가?")

print()

print("2. 위 키워드로 아래의 장르 중 어떤 장르의 정보를 수집할까요?")
print()
print("\t" + "1.학위 논문" + "\t" + "2.국내학술논문" + "\t" + "3.해외학술논문" + "\t" + "4.학술지")
print("\t" + "5.단행본" + "\t" + "6.공개강의" + "\t" + "7.연구보고서")
n = int(input("위 장르 중 수집할 장르의 번호를 입력하세요:"))

genreList = ['학위 논문','국내학술논문','해외학술논문','학술지','단행본','공개강의','연구보고서']
genre = genreList[n - 1]

print()
fx_txt = input("결과를 저장할 txt형식의 파일명을 쓰세요(예: c:\\tmp\\riss.txt): ")
print()

#1
chrome_path = "C:\\tmp\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = 'http://www.riss.kr/'
driver.get(url)
time.sleep(2)

#2
element = driver.find_element_by_id("query")
driver.find_element_by_id("query").click()
element.send_keys(query_txt)
element.send_keys("\n")
time.sleep(2)

#3
driver.find_element_by_link_text(genre).click()
time.sleep(2)

#4
from bs4 import BeautifulSoup
import math
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
total_cnt = soup.find('div','searchBox').find('span','num').get_text()

print(f'{query_txt} 키워드로 국내학술논문 부분에서 검색된 자료의 건수는 총 {total_cnt}건 입니다')
collect_cnt = int(input("이 중에서 크롤링 할 건수는 몇건입니까?:"))
collect_page_cnt = math.ceil(collect_cnt / 10)
print(f'{query_txt} 키워드로 {genre}을 검색하여 총 {total_cnt}건 중 {collect_cnt}건의 정보를 수집하겠습니다.')
print(f'{collect_page_cnt}페이지를 탐색합니다.')

#5

page_no = []
no = 1
for i in range(10,collect_cnt):
    if i % 10 == 0:
        page_no.append(i + 1)
        
for a in range(1,collect_page_cnt + 1):
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    content = soup.find('div','srchResultListW').find_all('li')

    for b in content:
        try:
            title = b.find('div','cont').find('p','title').get_text()
        except:
            continue
        else:
            f = open(fx_txt,'a',encoding='UTF-8')
            
            print(f'1.번호:{no}\n')
            f.write(f'1.번호:{no}\n')
            
            print(f'2.제목:{title}\n')
            f.write(f'2.제목:{title}\n')
            
            writer = b.find('span','writer').get_text()
            print(f'3.작성자:{writer}\n')
            f.write(f'3.작성자:{writer}\n')
            
            assigned = b.find('span','assigned').get_text()
            print(f'4.소속기관:{assigned}\n')
            f.write(f'4.소속기관:{assigned}\n')
            
            year = b.find('p','etc').select('span')[2].get_text()
            print(f'5.발표년도:{year}\n')
            f.write(f'5.발표년도:{year}\n');
            
            f.write('\n')
            
        no += 1
        
        if no > collect_cnt:
            break
        
        time.sleep(1)

c = math.floor(a/10)-1

a += 1

if a == page_no[c]:
    driver.find_element_by_link_text('다음 페이지로').click()
else:
    driver.find_element_by_link_text('%s'%a).click()
