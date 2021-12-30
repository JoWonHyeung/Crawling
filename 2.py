from selenium import webdriver
import time

query_text = input("1. 수집할 자료의 키워드는 무엇입니까?")
print("\n")

chrome_path = "C:\\tmp\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = 'https:\\www.naver.com'
driver.get(url)
time.sleep(2)

element = driver.find_element_by_name("query")
driver.find_element_by_name("query").click()
element.send_keys(query_text)
element.send_keys("\n")