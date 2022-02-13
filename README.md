# WebCrawling

### -웹 크롤링의 원리-
1. 파이썬 언어로 Selenium에게 특정 웹 페이지를 크롤링하라고 명령한다
2. Selenium은 Web Driver를 실행하여 웹페이지에 접속
3. 웹페이지를 현재 컴퓨터로 가져온다
4. Beautiful soup을 이용하여 필요한 부분만 골라온다.
5. 골라낸 데이터를 원하는 파일 형태로 저장한다

### -웹 페이지의 특정 element에 접근하는 다양한 방식들-
find_element_by_id

find_element_by_name

find_element_by_xpath

find_element_by_css_selector

find_element_by_class_name

find_element_by_tag_name

find_element_by_link_text

### -Beautiful soup를 사용하여 데이터 추출하기-
1) find() : 주어진 조건을 만족하는 첫 번째 태그 값만 가져오기
2) find_all() : 해당 태그가 여러 개 있을 경우 한꺼번에 모두 가져오기
3) select() : css selector를 활용해서 원하는 태그를 찾는 방법. 자세한 방법은 책 참고할 것
4) .string or .get_text()를 사용해서 text만 추출할 수 있다.

### -driver 실행시 오류 메세지 제거-
```python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(chrome_path,options=options)
driver.maximize_window()
```

### - pyinstaller 오류 해결
- https://stackoverflow.com/questions/44740792/pyinstaller-no-module-named-pyinstaller

# 실습 내용

### 1.py / 2.py
 'http://www.riss.kr/' 사이트에서 입력한 키워드로 논문을 검색하고 데이터를 수집하였다.

 
### 3.py
 'https://datalab.naver.com/' 에서 분야별 인기 검색어 Top500에서 데이터를 수집하였다.

### 4.py
 인스타그램에서 해시태그 정보를 수집하였다.
 
 - 스크롤 다운 함수 
 ```python
 def scroll_down(browser):
    broswer.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)
 
 i = 1
 while i <= cnt:
    scroll_down(broswer)
    i += 1
 ```
  - 비트맵 이미지 아이콘을 위한 대체 딕셔너리 생성
 ```python
 import sys
 bmp_map = dict.fromkeys(range(0x10000,sys.maxunicode + 1), 0xfffd)
 ```
   - 글자로 변환 후 글자가 분리되지 않도록 normalize해준다.
 ```python
 tags = tags_1[d].get_text()
 tags_11 = tags.translate(bmp_map)
 tags_2 = unicodedata.normalize('NFC',tags_11)
 ```
 
