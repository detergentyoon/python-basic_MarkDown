# **`1-1. Python`**
다른 언어에 비해 사용하기가 아주 쉬운 Python의 기본 문법과 실생활 기반 예제, Part 별 퀴즈 등 Youtube 나도코딩님의 파이썬 기본편 강의를 공부한 내용을 MarkDown으로 정리했습니다.

# **`2-1. 숫자 자료형`**
```python
print(5) # 5
print(-10) # -10
print(3.14) # 3.14
print(100) # 100
print(5+3) # 8
print(2*4) # 8
print(3*(3+1)) # 12
```
<br>

---
# **`2-2. 문자열 자료형`**
```python
print('Python') # Python
print("Python") # Python
print("Python"*3) # PythonPythonPython
```
<br>

---
# **`2-3. boolean 자료형`**
```python
# 참 / 거짓
print(5 > 10) # False
print(5 < 10) # True
print(True) # True
print(False) # False
print(not True) # False
print(not False) # True
print(not (5 > 10)) # True
```
<br>

---
# **`2-4. 변수(variable)`**
```python
# 애완동물을 소개합니다

animal = "강아지"
name = "파이썬"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "입니다.")
print(name + "은 " + str(age) + "살이며, " + hobby + "을 아주 좋아합니다.")
print(name + "은 어른일까요? " + str(is_adult))

# 우리집 강아지의 이름은 파이썬입니다.
# 파이썬은 4살이며, 산책을 아주 좋아합니다.
# 파이썬은 어른일까요? True
```
변수의 값만 수정하여 출력문을 수정할 수 있습니다.
```python
animal = "고양이"
name = "리눅스"
age = 2
hobby = "낮잠"
is_adult = age >= 3

# 우리집 고양이의 이름은 리눅스입니다.
# 리눅스은 2살이며, 낮잠을 아주 좋아합니다.
# 리눅스은 어른일까요? False
```
\+ 대신 , 을 사용할 수 있습니다. 이 경우 **정수형 변수나 boolean 변수를 str()로 감싸주지 않고도 출력이 가능**하지만 **변수의 끝에 공백이 붙습니다.**
```python
print(name, "은 ", age, "살이며, ", hobby, "을 아주 좋아합니다.")
# 리눅스 은  2 살이며,  낮잠 을 아주 좋아합니다.
```
<br>

---
# **`2-5. 주석`**
```python
# 한 줄 주석

''' 여러
줄
주석 '''
```
<br>

---
# **`3-1. 연산자 & 수식`**
+ add . sub . mul . div
```python
print(1 + 1) # 2
print(3 - 2) # 1
print(5 * 2) # 10
print(6 / 3) # 2
```

+ pow . rem . quo
```python
print(2 ** 3) # 2^3 = 8
print(5 % 3) # 나머지 2
print(5 // 3) # 몫 1
```

+ equal sign . inequality sign
```python
print(10 == 3) # False
print(4 <= 7) # True
print(3 > 5) # False
```

+ and . or . not
```python
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 < 5)) # True
print((3 > 0) | (3 < 5)) # True

print(not(1 != 3)) # False
```
<br>

---
# **`3-2. 숫자 처리 함수`**
+ 절대값 . 제곱 . 최댓값 . 최솟값 . 반올림
```python
print(abs(-5)) # 5
print(pow(4,2)) # 4^2 = 4*4 = 16
print(max(3,7)) # 7
print(min(3,7)) # 3
print(round(3.14)) # 3
print(round(4.99)) # 5
```
+ Python에서 제공하는 math 라이브러리 사용
```python
from math import *
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근. 4
```
<br>

---
# **`3-3. 랜덤 함수(random function)`**
```python
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성

print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(randrange(1,10) # 1 ~ 10 미만의 임의의 값 생성

print(randint(1,10)) # 1 ~ 10 이하의 임의의 값 생성
```
<br>

---
# **`Part 3 퀴즈`**
당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.  
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.  
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.  

+ 조건 1 : 랜덤으로 날짜를 뽑아야 함
+ 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
+ 조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외  

## **출력예제**
```python
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
```

## **정답코드**
```python
from random import *

date = randint(1, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")
```
<br>

---
# **`4-1. 문자열(string)`**
```python
sentence = '나는 코더입니다'
sentence2 = "파이썬은 쉬워요"
sentence3 = """
나는 코더이고
파이썬은 쉬워요
"""
```
<br>

---
# **`4-2. 슬라이싱(slicing)`**
```python
info = "990428-1234567"

print("연 : " + info[:2]) # 0 부터 2 직전까지 (0, 1)
print("월 : " + info[2:4])
print("일 : " + info[4:6])
print("생년월일 : " + info[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + info[7:]) # 7 부터 끝까지
print("뒤 7자리(뒤에부터) : " + info[-7:]) # 맨 뒤에서 7번째부터 끝까지
```
<br>

---
# **`4-3. 문자열 처리 함수`**
```python
python = "Python is Amazing"
print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # True
print(len(python)) # 17
print(python.replace("Python", "Java")) # Java is Amazing

index = python.index("n")
print(index) # 5
index = python.index("n", index + 1)
print(index) # 15

print(python.find("java")) # 없는 문자를 검색하면 -1 출력
print(python.index("java")) # 없는 문자를 검색하면 오류 > 프로그램 종료

print(python.count("n")) # 2
```
<br>

---
# **`4-4. 문자열 포맷(str.format)`**
## 방법 1
+ 정수 
```python
print("나는 %d살입니다." % 20)
# 나는 20살입니다.
```
+ 문자
```python
print("Apple 은 %c로 시작해요." % "A")
# Apple 은 A로 시작해요.
```
+ 문자열
```python
print("나는 %s을 사용해요." % "Python")
# 나는 Python을 사용해요.
print("나는 %s살입니다." % 20)
# 나는 20살입니다.
print("나는 %s색과 %s색을 좋아해요." % ("흰", "검은"))
# 나는 흰색과 검은색을 좋아해요.
```
## 방법 2
```python
print("나는 {}살입니다.".format(20))
# 나는 20살입니다.

print("나는 {}색과 {}색을 좋아해요.".format("흰", "검은"))
print("나는 {0}색과 {1}색을 좋아해요.".format("흰", "검은"))
# 나는 흰색과 검은색을 좋아해요.

print("나는 {1}색과 {0}색을 좋아해요.".format("흰", "검은"))
# 나는 검은색과 흰색을 좋아해요.
```
## 방법 3
```python
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "검은"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "검은", age = 20))
# 나는 20살이며, 검은색을 좋아해요.
```
## 방법 4
```python
age = 20
color = "검은"

print(f"나는 {age}살이며, {color}색을 좋아해요.")
# 나는 20살이며, 검은색을 좋아해요.
```
<br>

---
# **`4-5 탈출문자(escape character)`**
`\n` : 줄바꿈
```python
print("백문이 불여일견\n백견이 불여일타")
# 백문이 불여일견
# 백견이 불여일타
```

`\"` , `\'` : 문장 내에서 따옴표  
```python
print("나는 \"온화한사람\"입니다.")
# 나는 "온화한사람"입니다.
print('나는 \'온화한사람\'입니다.')
# 나는 '온화한사람'입니다.
```
`\\` : 문장 내에서 \
```python
print("C:\\Users\\mildMan\\Desktop\\PythonWorkspace>")
# C:\Users\mildMan\Desktop\PythonWorkspace>
```
`\r` : 커서를 맨 앞으로 이동
```python
print("Red Apple\rPine")
# PineApple
```
`\b` : 백스페이스 (한 글자 삭제)
```python
print("Redd\b Apple")
# Red Apple
```
`\t` : 탭
```python
print("Red\tApple")
# Red     Apple
```
<br>

---
# **`Part 4 퀴즈`**
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

예) http://naver.com

+ 규칙 1 : http:// 부분은 제외<br>=> naver.com
+ 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외<br>=> naver
+ 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성<br>=> nav + 5 + 1 + !

## **출력예제**
예) 생성된 비밀번호 : nav51!

## **정답코드**
```python
url = "http://naver.com"

rule = url.replace("http://", "")
rule = rule[:rule.index(".")]
password = rule[:3] + str(len(rule)) + str(rule.count("n")) + "!"

print(password)
```
<br>

---
# **`5-1. 리스트 자료형(list)`**
[ ] 로 값을 묶어놓은 클래스
```python
subway = [10, 20, 30]
print(subway)
# [10, 20, 30]
```
+
```python
subway = ["유재석", "조세호", "박명수"]
print(subway)
# ['유재석', '조세호', '박명수']


# 조세호는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))
# 1


# 하하가 다음 정류장에서 다음 칸에 탑승
subway.append("하하")
print(subway)
# ['유재석', '조세호', '박명수', '하하']


# 정형돈이 유재석 / 조세호 사이에 탑승
subway.insert(1, "정형돈")
print(subway)
# ['유재석', '정형돈', '조세호', '박명수', '하하']


# 지하철에 있는 사람이 한 명씩 뒤에서 하차
subway.pop()
print(subway)
# ['유재석', '정형돈', '조세호', '박명수']


# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
# ['유재석', '정형돈', '조세호', '박명수', '유재석']
print(subway.count("유재석"))
# 2


# 리스트 정렬
num_list = [5,2,4,1,3]
num_list.sort()
print(num_list)
# [1, 2, 3, 4, 5]


# 리스트 순서 뒤집기
num_list.reverse()
print(num_list)
# [5, 4, 3, 2, 1]


# 모두 지우기
num_list.clear()
print(num_list)
# []


# 다양한 자료형과 함께 사용
num_list = [5, 2, 4, 1, 3]
mix_list = ["조세호", 20, True]


# 리스트 확장
num_list.extend(mix_list)
print(num_list)
# [5, 2, 4, 1, 3, '조세호', 20, True]
```
<br>

---
# **`5-2. 사전 자료형(dict)`**
key 와 value 를 포함한 { } 의 형태로 묶어놓은 클래스로, key 의 중복이 불가능함
```python
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet)
# {3: '유재석', 100: '김태호'}
```
## 값을 가져오는 방법 1 : `[ ]`
```python
print(cabinet[3])
# 유재석
```
## 값을 가져오는 방법 2 : `get`
```python
print(cabinet.get(3))
# 유재석
```

### 값을 가져올 때 없는 값을 가져오려 하면
+ **[ ]** 의 경우 KeyError가 발생하며 프로그램이 종료됨.
+ **get** 의 경우 None 을 출력하고 프로그램이 종료되지 않음.
```python
print(cabinet[5])
# KeyError: 5   => 이후 프로그램 종료
print(cabinet.get(5))
# None

# key 가 없는 값을 출력할 때 None 대신 다른 문장을 출력도 가능
print(cabinet.get(5, "사용가능"))
# 사용가능
```

## 사전 자료형 안에 어떤 값이 있는지 확인
```python
print(3 in cabinet) # Ture
print(5 in cabinet) # False
```

## 정수가 아닌 스트링 형태 구성도 가능
```python
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호
```

## 추가 / 변경 / 삭제하기
```python
cabinet["C-20"] = "조세호" # 추가
cabinet["A-3"] = "김종국" # 변경
del cabinet["B-100"] # 삭제
print(cabinet)
# {'A-3': '김종국', 'C-20': '조세호'}
```

## key 만 출력
```python
print(cabinet.keys())
# dict_keys(['A-3', 'C-20'])
```
## value 만 출력
```python
print(cabinet.values())
# dict_values(['김종국', '조세호'])
```
## key & value 모두 출력
```python
print(cabinet.items())
# dict_items([('A-3', '김종국'), ('C-20', '조세호')])
```
## 초기화
```python
cabinet.clear()
print(cabinet)
# {}
```
<br>

---
# **`5-3. 튜플 자료형(tuple)`**
튜플은 리스트와 다르게 내용을 변경이나 추가할 수 없지만 처리 속도는 리스트보다 빠르기 때문에, <u>변경되지 않는 목록</u>을 활용할 때 주로 튜플을 사용합니다.
```python
menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스
```
## 코딩 방법 1
```python
name = "mildMan"
age = 23
hobby = "Game"
print(name, age, hobby) # mildMan 23 Game
```
## 코딩 방법 2
```python
(name, age, hobby) = ("mildMan", 23, "Game")
print(name, age, hobby) # mildMan 23 Game
```
<br>

---
# **`5-4. 집합 자료형(set)`**
집합(set)은 **중복이 불가능**하고, **순서가 없는** 것이 특징인 자료형입니다.
<br>
<br>
## **코딩 방법**
```python
temp = {1,2,3,3,3}
print(temp) # {1, 2, 3}   => '3' 이 중복되지 않음

java = {"유재석", "김태호", "양세형"} # 방법 1
python = set(["유재석", "박명수"]) # 방법 2

# 방법 2 처럼 list 형태로 먼저 만들고 나서 set() 로 묶어줄 수도 있습니다.
```
## **교집합** (java 와 python 을 모두 할 수 있는 개발자)
```python
print(java & python)
print(java.intersection(python))
# {'유재석'}
```
## **합집합** (java 혹은 python 을 할 수 있는 개발자)
```python
print(java | python)
print(java.union(python))
# {'박명수', '양세형', '김태호', '유재석'}
```
## **차집합** (java 는 할 수 있지만 python 은 할 줄 모르는 개발자)
```python
print(java - python)
print(java.difference(python))
# {'양세형', '김태호'}
```
## **추가** (python 을 할 수 있는 개발자가 늘어남)
```python
python.add("김태호")
print(python) # {'유재석', '김태호', '박명수'}
```
## **삭제** (java 사용법을 잊어버린 개발자)
```python
java.remove("김태호")
print(java) # {'유재석', '양세형'}
```
<br>

---
# **`5-5. 자료구조의 변경`**
```python
menu = {"커피", "우유", "주스"}

print(menu, type(menu))
# {'우유', '주스', '커피'} <class 'set'>

menu = list(menu)
print(menu, type(menu))
# ['주스', '커피', '우유'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu))
# ('커피', '우유', '주스') <class 'tuple'>

menu = set(menu)
print(menu, type(menu))
# {'커피', '우유', '주스'} <class 'set'>
```
<br>

---
# **`Part 5 퀴즈`**
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건 3 : random 모듕ㄹ의 shuffle 과 sample 을 활용

## **출력예제**
```python
 -- 당첨자발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
 -- 축하합니다 --
```

## **정답코드**
```python
from random import *

user = range(1, 21)
user = list(user)

shuffle(user)
choosenUser = sample(user, 4)

print(" -- 당첨자발표 --")
print(f"치킨 당첨자 : {choosenUser[0]}")
print(f"커피 당첨자 : {choosenUser[1:]}")
print(" -- 축하합니다 --")
```
<br>

---
# **`6-1. 조건문(if)`**
## **코딩 방법**
```python
변수 = "비"
if 조건 :
  실행 명령문
```
## **예제 1** ("오늘 날씨는 어때?")
```python
weather = input("How's the weather today?\n")

if weather == "rainy" or weather == "snowy" :
  print("Take a umbrella.")
elif weather == "air pollution" :
  print("Take a mask")
else :
  print("It's up to you.")
```
## **예제 2** ("오늘 기온은 어때?)
```python
temp = int(input("How's the temperature today?\n"))
if 30 <= temp :
  print("It's too hot. don't go outside.")
elif 10 <= temp & temp < 30 :
  print("It's a nice day.")
elif 0 <= temp < 10 :
  print("I'll have to put on my coat.")
else :
  print("It's too cold. don't go outside.")
```
<br>

---
# **`6-2. 반복문 : for`**
## **예제 1** (같은 문장 count 출력)
```python
cnt = list(range(0, 6))

for i in cnt :
  print(f"{i}th output")

# 0th output
# 1th output
# ...
# 5th output
```
## **예제 2** ("OO님, 주문하신 커피 나왔습니다.")
```python
customer = ["Alice", "Kiki", "Howl"]

for i in customer :
  print(f"{i}님, 주문하신 커피 나왔습니다.")

# Alice님, 주문하신 커피 나왔습니다.
# Kiki님, 주문하신 커피 나왔습니다.
# Howl님, 주문하신 커피 나왔습니다.
```
<br>

---
# **`6-3. 반복문 : while`**
## **코딩 방법**
```python
while (조건) :
  (출력)
```
## **예제 1** (폐기처분 커피)
***조건 1** : 손님이 주문하신 커피가 완성되면 2분 간격으로 손님을 호출*  
***조건 2** : 10분이 지나도 손님이 받으러 오시지 않으시면 커피를 폐기처분함*
```python
customer = "Alice"
i = 10

while i >= 1 :
  print(f"{customer}님, 커피 나왔습니다. (남은 시간 : {i}분)")
  i -= 2
  if i == 0 :
    print(f"{customer}님의 커피는 폐기처분 되었습니다.")

# Alice님, 커피 나왔습니다. (남은 시간 : 10분)
# Alice님, 커피 나왔습니다. (남은 시간 : 8분)
# Alice님, 커피 나왔습니다. (남은 시간 : 6분)
# Alice님, 커피 나왔습니다. (남은 시간 : 4분)
# Alice님, 커피 나왔습니다. (남은 시간 : 2분)
# Alice님의 커피는 폐기처분 되었습니다.
```
## **예제 2** (무한루프)
반복문이 끝도 없이 반복되는 것을 '무한루프에 빠졌다' 라고 합니다.  
무한루프 도중 터미널에 Ctrl + C 를 입력하면 키보드인터럽트를 통해 프로그램을 강제로 중지시킬 수 있습니다.
```python
i = 1
while 1 : # 1 혹은 True 
  print(f"{i}회")
  i += 1

# 1회
# 2회
# 3회
# ...
```
## **예제 3** (커피를 받으러 온 손님이 음료를 주문한 손님이 맞는지 확인하기)
조건 : while문의 조건과 일치하기 전까지 무한루프를 돌림
```python
customer = "Alice"
guestID = "unknown"

while guestID != customer :
  print(f"{customer}님, 커피가 준비 되었습니다.")
  guestID = input("고객님 ID가 어떻게 되세요?\n")

# Alice님, 커피가 준비 되었습니다.
# 고객님 ID가 어떻게 되세요?
# mildMan   => guest 와 input 값이 서로 다르기 때문에 다시 반복

# Alice님, 커피가 준비 되었습니다.
# 고객님 ID가 어떻게 되세요?
# Alice   => guest 와 input 값이 서로 동일하여 반복문 종료
```
<br>

---
# **`6-4. continue & break`**
## **예제 1** (출석체크)
***조건** : 결석자를 제외한 학생만 출석을 부름*
```python
absent = [3, 5] # 결석자

for i in range(1,7) :
  if i in absent :
    continue
  print(f"{i}번 출석")

# 1번 출석
# 2번 출석
# 4번 출석
# 6번 출석
```
## **예제 2** (수업 강제 종료)
***조건** : 무서운 선생님께서는 교과서를 안가져온 학생이 있으면 수업을 끝내버림*
```python
absent = [3, 5] # 결석자
no_book = [4] # 교과서 미지참자

for i in range(1,7) :
  if i in absent :
    continue
  if i in no_book :
    print(f"오늘 수업 여기까지. {i}번은 교무실로 따라와.")
    break
  print(f"{i}번 출석")

# 1번 출석
# 2번 출석
# 오늘 수업 여기까지. 4번은 교무실로 따라와.
```
<br>

---
# **`6-5. 6한 줄 for`**
## **예제 1** (출석번호 앞에 100 붙이기)
```python
student = list(range(1,6))

student = [i+100 for i in student]
print(student) # [101, 102, 103, 104, 105]
```
## **예제 2** (이름을 길이로 변환)
```python
cnt = ["Iron man","Thor","Captain america"]

cnt = [len(i) for i in cnt]
print(cnt) # [8, 4, 15]
```
## **예제 3** (이름을 대문자로 변환)
```python
cnt = ["Iron man","Thor","Captain america"]

cnt = [i.upper() for i in cnt]
print(cnt) # ['IRON MAN', 'THOR', 'CAPTAIN AMERICA']
```
<br>

---
# **`Part 6 퀴즈`**
당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.  
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

***조건 1** : 승객 별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.*  
***조건 2** : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.*

### **출력문 예제**
```python
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...  
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2명
```
### **정답 코드**
```python
from random import *

guest = 0

for i in range(1, 51) :
  time = randrange(5, 51)
  if 5 <= time <= 15 :
    print(f"[O] {i}번째 손님 (소요시간 : {time}분)")
    guest += 1
  else :
    print(f"[ ] {i}번째 손님 (소요시간 : {time}분)")

print(f"총 탑승 승객 : {guest}명")
```
<br>

---
# **`7-1. 함수`**
## **코딩 방법**
```python
# 정의
def function_name() :
  output process

# 호출
function_name()
```
<br>

---
# **`7-2. 전달값과 반환값`**
함수 내에서 동작한 매개변수는 함수를 탈출함과 동시에 사라집니다.  
때문에 함수 안에서 동작한 값을 밖에서도 활용하기 위해 반환값(**return**)을 사용합니다.
## **예제 1-1** (현금 입출금)
```python
def deposit(balance, money): # 입금
  print(f"입금 완료. 잔액 : {balance + money}원")
  return balance + money

balance = 0 # 잔액
balance = deposit(balance, 1000) # 1000원 입금의 함수 동작 결과를 return 을 통해 가져옴
print(f"{balance}원")
# 입금 완료. 잔액 : 1000원
# 1000원

def withdraw(balance, money):
  if balance >= money :
    print(f"출금 완료 | 잔액 : {balance - money}원")
    return balance - money
  else :
    print(f"잔액 부족 | 잔액 : {balance}원")
    return balance

# balance < money process
balance = withdraw(balance, 5000)
print(f"{balance}원")
# 잔액 부족 | 잔액 : 1000원
# 1000원

# balance >= money process
balance = withdraw(balance, 700)
print(f"{balance}원")
# 출금 완료 | 잔액 : 300원
# 300원
```
## **예제 1-2** (수수료가 붙는 야간 시간 현금 출금)
```python
def withdraw_night(balance, money):
  commission = 100 # 수수료 100원
  if balance >= money :
    print(f"야간 시간 출금에는 수수료 {commission}원이 청구됩니다.")
    print(f"출금 완료 | 잔액 : {balance - money - commission}원")
    return commission, balance - money - commission  # tuple 형태로 여러 개의 값 반환
  else :
    print(f"잔액이 모자랍니다 | 잔액 : {balance}원")
    return balance

balance = 0
balance = deposit(balance, 10000)
# 입금 완료 | 잔액 : 10000원

commission, balance = withdraw_night(balance, 500)
print(f"수수료 : {commission}원 | 잔액 : {balance}원")
# 야간 시간 출금에는 수수료 100원이 청구됩니다.
# 출금 완료 | 잔액 : 9400원
# 수수료 : 100원 | 잔액 : 9400원
```
<br>

---
# **`7-3. 함수의 기본값`**
## **예제** (같은 학년, 같은 반 프로필 기본값)
```python
def profile(name, age=17, main_lang="Python"): # 함수의 매개변수에 미리 값을 지정해놓으면
  print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")

profile("유재석") # 값 지정해두지 않은 매개변수만 불러와도 나머지 매개변수들의 값은 미리 지정해둔 값으로 출력
profile("박명수")
# 이름 : 유재석   나이 : 17       주 사용 언어 : Python
# 이름 : 박명수   나이 : 17       주 사용 언어 : Python
```
<br>

---
# **`7-4. 키워드값`**
함수에서 전달받는 매개변수의 값을 키워드를 이용해서 함수를 호출하면(키워드=값)
그 키워드에 해당하는 값이 순서가 뒤섞여있어도 정의한 함수의 순서대로 출력됨
```python
def profile(name, age, main_lang):
  print(name, age, main_lang)

profile(name="유재석", main_lang="Python", age=20)
profile(main_lang="Java", age=25, name="김태호")
# 유재석 20 Python
# 김태호 25 Java
```
<br>

---
# **`7-5. 가변인자를 이용한 함수 호출`**
서로 다른 갯수의 값을 넣어줄 때는 가변인자(*로 시작되는 매개변수)를 사용

## **예제** (사용 가능한 프로그래밍 언어 갯수)
```python
def profile(name, age, *language):
  print(f"이름 : {name}\t나이 : {age}\t", end=" ") # end=" " : 출력문이 줄바꿈이 되지 않고 나란히 나오도록 하는 용도
  for lang in language:
    print(lang, end=" ")
  print() # 줄바꿈

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
profile("박명수", 25, "Kotlin", "Swift")
# 이름 : 유재석   나이 : 20        Python Java C C++ C# Javascript 
# 이름 : 박명수   나이 : 25        Kotlin Swift
```
<br>

---
# **`7-6. 지역변수와 전역변수`**
+ 지역변수 : 함수 내에서만 사용이 가능하고, 함수 밖으로 탈출하면 사라지는 변수  
+ 전역변수 : 프로그램 어느 곳에서나 호출할 수 있는 변수
<br>
<br>
지역변수 값을 함수 밖에서도 활용하기 위해 다음과 같은 코드를 취할 수 있습니다.
1. 정의해둔 전역변수를 함수 내에서 global 로 호출 선언
1. 매개변수의 값을 return 을 통해 함수 밖으로 반환

## **예제** (총기함에 보관된 남은 총의 갯수)
```python
gun = 10

def checkpoint(soldiers): # 경계 근무를 나가는 2명의 군인
  global gun # 전역 공간에 있는 'gun' 변수를 사용하겠음을 선언
  gun = gun - soldiers
  print(f"[함수 내] 남은 총 : {gun}정")

def checkpoint_ret(gun, soldiers):
  gun = gun - soldiers
  print(f"[함수 내] 남은 총 : {gun}정")
  return gun

print(f"전체 총 : {gun}정") #   => 10정
checkpoint(2) #   => 8정
gun = checkpoint_ret(gun, 2) #   => 6정
print(f"남은 총 : {gun}")

# 전체 총 : 10정
# [함수 내] 남은 총 : 8정
# [함수 내] 남은 총 : 6정
# 남은 총 : 6
```
<br>

---
# **`Part 7 퀴즈`**

Quiz) 표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
  남자 : 키(m) x 키(m) x 22
  여자 : 키(m) x 키(m) x 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째 자리로 표시

## **(출력 예제)**
키 175cm 남자의 표준 체중은 67.38kg 입니다.

## **정답 코드**
```python
def std_weight(height, gender):
  if gender == "남자" :
    return height * height * 22
  elif gender == "여자" :
    return height * height * 21

height = 175
gender = "남자"
weight = std_weight(height / 100, gender)

print(f"키 {height}cm {gender}의 표준 체중은 {weight:.2f}kg입니다.")

height = 175
gender = "여자"
weight = std_weight(height / 100, gender)

print(f"키 {height}cm {gender}의 표준 체중은 {weight:.2f}kg입니다.")
```
<br>

---
# **`8-1. 표준 입출력`**
## **sys**
```python
import sys

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# Python Java
```
VScode의 터미널에서는 두 출력문의 차이가 없는 것처럼 보이지만, 실제로는 아래와 같이 처리됩니다.
+ stdout : 표준 출력으로 처리
+ stderr : 표준 에러로 처리
  + 만약 로그 처리를 하는 경우에는 에러(stderr)를 확인하고 따로 처리  
<br>

## **ljust() & rjust()**
>ljust() : n칸의 공백을 생성하고 좌측 정렬  
rjust() : n칸의 공백을 생성하고 우측 정렬
```python
scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items():
  print(subject.ljust(8), str(score).rjust(4), sep=":")

# 수학      :   0
# 영어      :  50
# 코딩      : 100
```
## **zfill()**
>zfill()은 입력한 int값 만큼 비어있는 자릿 수마다 0을 생성합니다.
```python
for num in range(1, 11):
  print("대기번호 : " + str(num).zfill(3))

# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
# ...
# 대기번호 : 009
# 대기번호 : 010
```
## **input**
>사용자입력(input)을 통해서 값을 받게되면 그 값이 어떤 형태의 자료형이라도 항상 문자열(str) 형태로 저장됩니다.
```python
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))

# 아무 값이나 입력하세요 : 10
# <class 'str'>

# 아무 값이나 입력하세요 : python
# <class 'str'>
```
<br>

---
# **`8-2. 다양한 출력 포맷`**
## **예제 1** : 빈 칸 공백, 우측 정렬, 총 10자리 공간 확보
```python
print("{0: >10}".format(500))
#       500
```

## **예제 2** : 빈 칸 공백, 우측 정렬, 부호 표시
```python
print("{0: >+10}".format(500))
#      +500
print("{0: >+10}".format(-500))
#      -500
```
## **예제 3** : 좌측 정렬, 빈 칸 _
```python
print("{0:_<10}".format(500))
# 500_______
```
## **예제 4-1** : 3자리 마다 콤마(,) 생성
```python
print("{0:,}".format(10000000000))
# 10,000,000,000
```
## **예제 4-2** : 3자리 마다 콤마(,) 생성, 부호 표시
```python
print("{0:+,}".format(10000000000))
# +10,000,000,000
print("{0:+,}".format(-10000000000))
# -10,000,000,000
```
## **예제 4-3** : 3자리 마다 콤마(,) 생성, 부호 표시, 자릿수 확보, 빈 칸 *
```python
print("{0:*<+30,}".format(10000000000))
# +10,000,000,000***************
```
## **예제 5** : 소수점 출력
```python
print("{0:f}".format(5/3))
# 1.666667
print("{0:.2f}".format(5/3))
# 1.67
```
<br>

---
# **`8-3. 파일 입출력`**
## **예제 1** : 파일 열기(생성) 및 작성, 파일 닫기
```python
score_file = open("score.txt", "w", encoding="utf8")
# open 을 통해서 파일 열기
# w(write) = '쓰기' 목적으로 열기
# utf8 = 한글 호환 출력

print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)

score_file.close()
# file 을 열었을 때는 항상 닫아주는 logic 을 구성해야함
```
## **출력 화면**
![score_file--opened](./img/score_file--opened.png)  
score.txt 파일이 생성되고 print 입력한 내용이 txt파일에 나타납니다.

<br>

## **예제 2** : 이전 파일에 이어 쓰기
```python
score_file = open("score.txt", "a", encoding="utf8")
# w(wirte) : 이전 파일에 덮어쓰기
# a(append) : 이전 파일에 이어 쓰기

score_file.write("과학 : 80")
score_file.write("코딩 : 100")
# var.write 를 통해 작성할 때에는 줄바꿈이 없음

score_file.close()

# 수학 : 0
# 영어 : 50
# 과학 : 80코딩 : 100
```
## **예제 3-1** : 파일 내용 읽기
>r(read) 를 통해 터미널로 파일의 내용을 불러올 수 있습니다.
```python
score_file = open("score.txt", "r", encoding="utf8")

print(score_file.read())

score_file.close()

# 수학 : 0
# 영어 : 50
# 과학 : 80코딩 : 100
```
## **예제 3-2** : readline()
```python
score_file = open("score.txt", "r", encoding="utf8")

print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())

score_file.close()

# 수학 : 0
#
# 영어 : 50
#
# 과학 : 80코딩 : 100
#
```
## **예제 4-1** while문을 통한 readline() 간편 제어
```python
score_file = open("score.txt", "r", encoding="utf8")

while True:
  line = score_file.readline()
  if not line: # 읽어올 내용이 없으면
    break
  print(line, end="") # end="" : print의 자동 줄바꿈 기능을 제외하기 위한 목적

score_file.close()

# 수학 : 0
# 영어 : 50
# 과학 : 80코딩 : 100
```
## **예제 4-2** readlines() 와 for문을 통한 간편 제어
>readlines() 는 파일 내용을 줄마다 list 형태로 저장합니다. 
```python
score_file = open("score.txt", "r", encoding="utf8")

lines = score_file.readlines() # list 형태로 저장
for line in lines:
  print(line, end="")

score_file.close()

# 수학 : 0
# 영어 : 50
# 과학 : 80코딩 : 100
```
<br>

---
# **`8-4. Pickle`**
>프로그램 상에서 내가 사용하고 있는 데이터를 file 형태로 저장해주는 것으로, 저장한 파일을 누군가에게 전달했을 때 파일 수신자가 파일을 열고 Pickle을 이용해 데이터를 불러와서 데이터를 재사용할 수 있게끔 도와주는 기능을 탑재한 라이브러리입니다.

## **예제 1** : Pickle 을 이용하여 데이터를 파일에 저장
```python
import pickle

profile_file = open("profile.pickle", "wb")
# b(binary) : pickle 을 사용할 때는 항상 binary type 을 정의해주어야 함
# pickle 에서는 따로 encoding 을 지정해줄 필요가 없음

profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
pickle.dump(profile, profile_file)
# pickle.dump() : 첫번째 인자에 있는 정보를 두번째 인자에 저장

profile_file.close()

### 즉, 내가 가진 정보를 피클을 이용해서 어떤 파일에 저장하는 과정 ###
```
## **예제 2** : Pickle 을 이용하여 파일에서 데이터 추출
```python
import pickle

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
# pickle.load() : file 에 들어있는 데이터를 profile 에 불러오기
print(profile) # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}

profile_file.close()

# 그 파일에 있는 내용을 load 를 통해 불러와서 변수에 저장을 해서 계속 사용할 수 있도록 도와주는 라이브러리
```
<br>

---
# **`8-5. with`**
>파일에 대한 처리를 할 때, with 를 사용하여 짧고 간결한 코드로 관리할 수 있습니다.
```python
import pickle

with open("profile.pickle", "rb") as profile_file: # pickle 파일 정보를 profile_file 에 저장
  print(pickle.load(profile_file))

# 따로 open 한 파일에 대해서 close() 를 하지 않아도 with문을 탈출함과 동시에 닫힘
```

```python
with open("study.txt", "w", encoding="utf8") as study_file:
  study_file.write("파이썬을 공부하고 있어요")
  # ( ) 안의 내용이 입력된 study.txt 생성

with open("study.txt", "r", encoding="utf8") as study_file:
  print(study_file.read())
  # 파이썬을 공부하고 있어요
```
<br>

---
# **`Part 8 퀴즈`**
당신의 회사에서는 매 주 1회 작성해야 하는 보고서가 있습니다.  
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.  
```python
- X 주차 주간보고 -
부서 :
이름 :
업무 요약 :
```
1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

***조건** : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.*

## **정답코드**
```python
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(f"- {i} 주차 주간보고 -")
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")
```
<br>

---
# **`9-1. 클래스(class)`**
![class_cookie](./img/class_cookie.png)  
##### `사진 및 클래스 설명 출처 https://wikidocs.net/28`
<br>

>클래스란 과자를 만드는 과자 틀과 같은 역할을 합니다.  
&nbsp;&nbsp;&nbsp;&nbsp; * 과자 틀 → 클래스 (class)  
&nbsp;&nbsp;&nbsp;&nbsp; * 과자 틀에 의해서 만들어진 과자 → 객체 (object)  

>클래스(class)란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면이고(과자 틀), 객체(object)란 클래스로 만든 피조물(과자 틀을 사용해 만든 과자)을 뜻합니다.

>클래스로 만든 객체는 객체마다 고유한 성격을 가집니다. 과자 틀로 만든 과자에 구멍을 뚫거나 조금 베어 먹더라도 다른 과자에는 아무 영향이 없는 것과 마찬가지로 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않습니다.

## **예제** : 게임 유닛 생성
```python
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # self.name 에 name 변수를 저장하여 초기화
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp} | 공격력 {self.damage}\n")

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
```
여기서 마린과 탱크는 Unit class 의 인스턴스(instance)다.' 라고 칭합니다.

<br>

---
# **`9-2. __init__`**
>__init__은 python에서 사용되는 생성자 함수입니다. **마린** 혹은 **탱크**와 같은 **어떠한 클래스(class)로부터 만들어지는 객체(object)가 생성될 때 자동으로 호출**됩니다.  
객체가 생성될 때는 기본적으로 init 함수에 정의된 개수와 동일한 수의 멤버변수 값을 전달해야 합니다. (<u>self 제외</u>)

```python
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp} | 공격력 {self.damage}\n")

# Error Ex)

marine3 = Unit("마린")
# TypeError: __init__() missing 2 required positional arguments: 'hp' and 'damage'
# 유형 오류: __init__()에 'hp' 및 'damage'라는 두 개의 필수 위치 인수가 없습니다.

marine4 = Unit("마린", 40, 5, "초과")
# TypeError: __init__() takes 4 positional arguments but 5 were given
# 유형 오류: __init__() 위치 인수가 4개 있지만 5개가 지정되었습니다.
```
<br>

---
# **`9-3. 멤버 변수(member variable)`**
>멤버 변수란 `self.name`, `self.hp`, `self.damage` 와 같이 값을 클래스 내에서 임의의 값을 할당할 수 있는 변수를 의미합니다.
```python
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp} | 공격력 {self.damage}\n")

wraith1 = Unit("레이스", 80, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")
# 유닛 이름 : 레이스, 공격력 : 5
```
`wraith1.name`, `wraith1.damage` 등 `.` 을 통해서 기존에 정의해둔 멤버 변수에 접근할 수 있습니다.

<br>

```python
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")
    # 레이스는 현재 클로킹 상태입니다.
if wraith1.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")
    # AttributeError: 'Unit' object has no attribute 'clocking'
```
`wraith2.clocking` 과 같이 어떠한 객체에 추가적인 변수를 클래스 외부에서 만들어 확장시킬 수 있습니다.

추가 변수 생성을 통해 객체를 확장시키는 동작 또한 기존에 있던 다른 객체에 대해서는 영향을 주지 못합니다.

<br>

---
# **`9-4. 메소드(method)`**
```python
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp} | 공격력 {self.damage}\n")

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name # name 은 전달받은 인자를 그대로 사용
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")
        # self.name, self.damage : class 자기 자신에 있는 멤버 변수의 값을 출력,
        # location : 전달받은 값을 출력

# 메소드 앞에는 무조건 self(자신)를 넣음
#
    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("1시")

firebat1.damaged(25)
firebat1.damaged(25)
```
<br>

---
# **`9-5. 상속`**
```python
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("1시")

firebat1.damaged(25)
firebat1.damaged(25)
```
<br>

---
# **`9-6. 다중 상속`**
```python
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
```
`AttackUnit` = `Unit` 상속  
`FlyableAttackUnit` = `AttackUnit` + `Flyable` 다중 상속

<br>

---
# **`9-7. 메소드 오버라이딩`**
>부모 클래스에서 정의한 메소드가 아닌 **자식 클래스에서 정의한 메소드를 새롭게 정의해서 사용**할 수 있는데 이를 메소드 오버라이딩이라고 합니다.
```python
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed : 0
        Flyable.__init__(self, flying_speed)

    # move() 재정의
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecrusier.move("9시")
```
`Unit`에 `move()` 함수 추가  

`Unit을 상속받은 AttackUnit`이 이동 => `Unit에서 정의한 move()` 함수 호출  

`AttackUnit을 상속받는 FlyableAttackUnit`이 이동 => `Unit에서 정의한 move()` 함수가 호출되는 것이 아니라, `FlyableAttackUnit에서 새로 정의한 move()` 함수가 호출됨.

<br>

---
# **`9-8. pass`**
>`pass`는 함수의 실제 logic은 생략시키지만 함수가 완성된 것 처럼 호출할 수 있게끔 만들어줍니다.
```python
def game_start():
    print("[알림] 새로운 게임 시작")

def game_over():
    pass

game_start() # [알림] 새로운 게임 시작
game_over() # 출력 없음
```
<br>

---
# **`9-9. super`**
>자신이 상속받는 부모 클래스의 멤버 변수를 초기화시킬 때 super를 통하여 부모 클래스명 대신 사용할 수 있습니다.

`super`는 `.__init__` 이전에 ( ) 를 붙이고, 멤버 변수에 `self`를 사용하지 않습니다.
```python
# 건물 생성
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)     => 기존의 Unit 을 이용한 __init__
        super().__init__(name, hp, 0) # super 를 통한 __init__은 멤버 변수에서 self를 제외
        self.location = location
```

<br>

`super`는 2개 이상의 부모 클래스를 **다중 상속받을 때는 순서 상의 맨 처음에 상속받는 클래스에 대해서만** `__init__` 함수가 호출됩니다.
### **다중 상속 못받는 super**
```python
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

dropship = FlyableUnit()
    # Unit 생성자
```
### **다중 상속을 받기 위해선 super 사용 x**
```python
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
    Unit.__init__(self) # 다중 상속의 경우 super 를 사용하지 않고 따로 명시
    Flyable.__init__(self)

dropship = FlyableUnit()
    # Unit 생성자
    # Flyable 생성자
```
<br>

---
# **`9-10. Starcraft.txt 프로젝트`**
## **유닛 생성, 제어 프로세스**
```python
from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성되었습니다.")

    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용할 수 없습니다.")

# 탱크
class Siege_Tank(AttackUnit):
    siege_mode_developed = False # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "시즈탱크", 150, 1, 35)
        self.siege_mode = False

    # 시즈모드 : 피해량 2배 증가
    def setSiegeMode(self):
        if Siege_Tank.siege_mode_developed == False:
            return

        # 시즈모드 비활성화 상태 => 시즈모드 활성화
        if self.siege_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.siege_mode = True
        # 시즈모드 활성화 상태 => 시즈모드 비활성화
        elif self.siege_mode == True:
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage /= 2
            self.siege_mode = False

        print(f"시즈모드를 활성화합니다. (이동 불가)")

# 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed : 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: # 클로킹 활성화 상태   => 클로킹 비활성화
            print(f"{self.name} : 클로킹 모드를 해제합니다.")
            self.clocked = False
        else: # 클로킹 비활성화 상태   => 클로킹 활성화
            print(f"{self.name} : 클로킹 모드로 전환합니다.")
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.\n")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")
    print("\n\t┌────────────────────┐")
    print("\t│      VICTORY !     │")
    print("\t└────────────────────┘")
```
<br>

## **임의 게임 진행 프로세스**
```python
# 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 시즈탱크 2기 생성
t1 = Siege_Tank()
t2 = Siege_Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛들을 소대 단위로 일괄 제어 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 소대 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Siege_Tank.siege_mode_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩 사용, 탱크 : 시즈모드 활성화, 레이스 : 클로킹 활성화)
for unit in attack_units:
    if isinstance(unit, Marine): # 유닛이 Marine 이면:
        unit.stimpack()
    elif isinstance(unit, Siege_Tank):
        unit.setSiegeMode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 소대 공격 (어택땅)
for unit in attack_units:
    unit.attack("1시")

# 소대가 전투 중 당하는 무작위 피해
for unit in attack_units:
    unit.damaged(randint(5, 30)) # 공격은 랜덤으로 받음 (5 ~ 30)

# 게임 종료
game_over()        
```
<br>

## **출력예시**
```python
[알림] 새로운 게임을 시작합니다.

마린 유닛이 생성되었습니다.
마린 유닛이 생성되었습니다.
마린 유닛이 생성되었습니다.
시즈탱크 유닛이 생성되었습니다.
시즈탱크 유닛이 생성되었습니다.
레이스 유닛이 생성되었습니다.
마린 : 1시 방향으로 이동합니다. [속도 1]
마린 : 1시 방향으로 이동합니다. [속도 1]
마린 : 1시 방향으로 이동합니다. [속도 1]
시즈탱크 : 1시 방향으로 이동합니다. [속도 1]
시즈탱크 : 1시 방향으로 이동합니다. [속도 1]
레이스 : 1시 방향으로 날아갑니다. [속도 : 5]
[알림] 탱크 시즈 모드 개발이 완료되었습니다.
마린 : 스팀팩을 사용합니다. (HP 10 감소)
마린 : 스팀팩을 사용합니다. (HP 10 감소)
마린 : 스팀팩을 사용합니다. (HP 10 감소)
시즈탱크 : 시즈모드로 전환합니다.
시즈모드를 활성화합니다. (이동 불가)
시즈탱크 : 시즈모드로 전환합니다.
시즈모드를 활성화합니다. (이동 불가)
레이스 : 클로킹 모드로 전환합니다.
마린 : 1시 방향으로 적군을 공격합니다. [공격력 5]
마린 : 1시 방향으로 적군을 공격합니다. [공격력 5]
마린 : 1시 방향으로 적군을 공격합니다. [공격력 5]
시즈탱크 : 1시 방향으로 적군을 공격합니다. [공격력 70]
시즈탱크 : 1시 방향으로 적군을 공격합니다. [공격력 70]
레이스 : 1시 방향으로 적군을 공격합니다. [공격력 20]
마린 : 17 데미지를 입었습니다.
마린 : 현재 체력은 13 입니다.
마린 : 30 데미지를 입었습니다.
마린 : 현재 체력은 0 입니다.
마린 : 파괴되었습니다.
마린 : 5 데미지를 입었습니다.
마린 : 현재 체력은 25 입니다.
시즈탱크 : 15 데미지를 입었습니다.
시즈탱크 : 현재 체력은 135 입니다.
시즈탱크 : 24 데미지를 입었습니다.
시즈탱크 : 현재 체력은 126 입니다.
레이스 : 14 데미지를 입었습니다.
레이스 : 현재 체력은 66 입니다.
Player : gg
[Player] 님이 게임에서 퇴장하셨습니다.

        ┌────────────────────┐
        │      VICTORY !     │
        └────────────────────┘
```
<br>

---
# **`Part 9 퀴즈`**
주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

## **출력예제**
```python
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
```

## **힌트코드**
```python
class House :
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass

    # 매물 정보 표시
    def show_detail(self):
        pass
```

## **정답코드**
```python
class House :
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print(f"총 {len(houses)}대의 매물이 있습니다.")
for house in houses:
    house.show_detail()
```