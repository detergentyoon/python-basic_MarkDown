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