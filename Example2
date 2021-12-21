from selenium import webdriver
from bs4 import BeautifulSoup 
import time

query_text = input("키워드를 검색하세요")

chrome_path = "C:\\tmp\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = "https:\\korean.visitkorea.or.kr"
driver.get(url)
time.sleep(2)

element = driver.find_element_by_id("inp_search")
driver.find_element_by_id("inp_search").click()
element.send_keys(query_text)
element.send_keys("\n")

html_1 = driver.page_source
soup_1 = BeautifulSoup(html_1, 'html.parser')

content_1 = soup_1.find('div','area_sWordList').find_all('li')

with open("C:\\tmp\\test3.txt","w", encoding="utf-8") as f:
    for i in content_1:
        f.write(i.get_text())
        f.write("\n")
        
f.close()


