# WebCrawling

### -웹 크롤링의 원리
1. 파이썬 언어로 Selenium에게 특정 웹 페이지를 크롤링하라고 명령한다
2. Selenium은 Web Driver를 실행하여 웹페이지에 접속
3. 웹페이지를 현재 컴퓨터로 가져온다
4. Beautiful soup을 이용하여 필요한 부분만 골라온다.
5. 골라낸 데이터를 원하는 파일 형태로 저장한다

### -웹 페이지의 특정 element에 접근하는 다양한 방식들
find_element_by_id

find_element_by_name

find_element_by_xpath

find_element_by_css_selector

find_element_by_class_name

find_element_by_tag_name

find_element_by_link_text

### -Beautiful soup를 사용하여 데이터 추출하기
1) find() : 주어진 조건을 만족하는 첫 번째 태그 값만 가져오기
2) find_all() : 해당 태그가 여러 개 있을 경우 한꺼번에 모두 가져오기
3) select() : css selector를 활용해서 원하는 태그를 찾는 방법. 자세한 방법은 책 참고할 것
4) .string or .get_text()를 사용해서 text만 추출할 수 있다.

### -driver 실행시 오류 메세지 제거
```python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(chrome_path,options=options)
driver.maximize_window()
```
### - pyinstaller 오류 해결
- https://stackoverflow.com/questions/44740792/pyinstaller-no-module-named-pyinstaller

### - VScode보다는 jupyter notebook으로 작업할 것
jupyter notebook은 코드를 작성하면 바로 실행 결과를 보여주기 때문에 시간을 굉장히 많이 줄일 수 있다.
하지만, 코드 자동 완성기능이 없어 매우 불편하다.

- jupyter notebook 실행 명령어
```python
python -m notebook

```

### - element vs elements
 
 driver.find_element_by_xxx : 조건에 맞는 요소 한 개 찾기, webElement 객체 리턴
 
 driver.find_elements_by_xxx : 조건에 맞는 모든 요소 찾기, list 객체 리턴
 
### - 요소의 정보 추출
 
element.tag_name : 태그명 추출

element.text : 텍스트 형식의 콘텐츠

element.get_attribute('속성명') : 속성값

### - Scroll Down

```python
# ActionChains 를 사용하기 위해서.
from selenium.webdriver import ActionChains

# id가 something 인 element 를 찾음
some_tag = driver.find_element_by_id('something')

# somthing element 까지 스크롤
action = ActionChains(driver)
action.move_to_element(some_tag).perform()

```

### - ect...

driver.implicitly_wait(3) : 경우에 따라 페이지 로드가 완료되거나 시작되기 전에 webdriver가 제어권을 반환 할 수 있다. 견고성을 확보하려면 explicit and impliciy waits를 사용하여 요소가 페이지에 존재할 때까지 대기

URL 인코딩 규칙을 적용해서 변환된 것을 서버에 전달
1. 영문, 숫자는 그대로
2. 한글은 16진수로 변환해서 전달
3. 공백문자는 + 기호로 변환해서 

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
 
 ### 5.ipynb 
  
   4.py에 이미지 수집기능을 추가하였다.
   
   urllib.request.urlretrieve(가져올 이미지 주소, 저장할 경로와 이름)

 - 이미지 수집
 ```python
import urllib.request
import urllib
try:
    photo = soup.find('div','KL4Bh').find('img')['src']
except:
    continue
else:
    urllib.request.urlretrieve(photo,image_path + str(file_no) + '.jpg')
    time.sleep(0.5)
    file_no += 1
 ```
 
 ### 6.ipynb
 https://thinkyou.co.kr 에서 공모전/대외활동 정보들을 수집한다. 현재 작업중인 WebProject에 실시간으로 공모전/대외활동 정보들을 사용자에게 제공할 예정이다.
 
- 마우스 이동
```python
from selenium.webdriver.common.action_chains import ActionChains

a = ActionChains(driver)
m= driver.find_element_by_xpath('//*[@id="gnb"]/li[1]/a/span')
a.move_to_element(m).perform()
```
    
 - UnicodeEncodeError 해결

한글 검색어를 아스키 코드로 표현할 수 없기 때문에 문제이다. 두 가지 해결 방법이 있으나, 첫 번째 방법만 소개하고 다른 해결 방법은 링크를 제공한다.
[해결 방안2](https://hengbokhan.tistory.com/25)

```python
from urllib.parse import quote

query = quote('테스트') #quote로 묶는다.
```

# Graph

- 그래프 색
```python
mycolormap = plt.cm.get_cmap('PuRd', 6) #RGBA 값을 튜플형태로 6SET를 반환한다.
print(type(mycolormap))
[mycolormap(i) for i in range(6)]
```

- matplotlib font 설정
```python
import matplotlib
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
# font_location = '/usr/share/fonts/truetype/nanum/NanumGothicOTF.ttf'
font_location = 'C:/Windows/Fonts/NanumGothic.ttf' # For Windows
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
```

- 단계구분도(Choropleth map)

각기 다른 음영이나 색상 또는 값으로 각 지역과 관련된 데이터를 표현한 지도

지도 데이터 파일 (.geojson) - 지역에 대한 경계 정보를 제공

시각화 하고자 하는 데이터 파일 (.csv 등) - 지역별로 표현하고자 하는 데이터를 제공

Choropleth와 같은 레이어를 만들 때 위의 이 두 데이터를 파라미터로 넘겨줘야 하는데 데이터는 각자 다른 파일에 있으므로, 시각화할 데이터를 지도에 얹으려면 두 데이터를 매핑해야 한다.

```python
folium.Choropleth(
geo_data = "지도 데이터 파일 경로 (.geojson, geopandas.DataFrame)"
data = "시각화 하고자 하는 데이터파일. (pandas.DataFrame)"
columns = (지도 데이터와 매핑할 데이터, 시각화 하고려는 데이터),
key_on = "지도 데이터 파일에서 데이터 파일과 매핑할 값 feature.properties.xxx",
fill_color = "시각화에 쓰일 색상",[fill_opacity=, line_opacity= ,]
legend_name = "칼라 범주 이름",
).add_to(m)
```

# KoNLPy 

- 한글 형태소 품사 태그표

http://kkma.snu.ac.kr/documents/?doc=postag

- 한국어 불용어

https://www.ranks.nl/stopwords/korean

# Apriori 알고리즘을 실행할 수 있도록 데이터 전처리

http://rasbt.github.io/mlxtend/user_guide/preprocessing/TransactionEncoder/
