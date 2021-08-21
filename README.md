# `숫자 자료형`
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

# `문자열 자료형`

```python
print('Python') # Python
print("Python") # Python
print("Python"*3) # PythonPythonPython
```
<br>

# `boolean 자료형`

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

# `변수`

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
+ 변수의 값만 수정하여 출력문을 수정할 수 있습니다.
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
+ \+ 대신 , 을 사용할 수 있습니다. 이 경우 **정수형 변수나 boolean 변수를 str()로 감싸주지 않고도 출력이 가능**하지만 **변수의 끝에 공백이 붙습니다.**
```python
print(name, "은 ", age, "살이며, ", hobby, "을 아주 좋아합니다.")
# 리눅스 은  2 살이며,  낮잠 을 아주 좋아합니다.
```
<br>

# `주석`
```python
# 한 줄 주석

''' 여러
줄
주석 '''
```
<br>

# `연산자`
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

# `숫자 처리 함수`
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

# `랜덤 함수`
```python
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성

print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(randrange(1,10) # 1 ~ 10 미만의 임의의 값 생성

print(randint(1,10)) # 1 ~ 10 이하의 임의의 값 생성
```

# `문자열`
```python
sentence = '나는 코더입니다'
sentence2 = "파이썬은 쉬워요"
sentence3 = """
나는 코더이고
파이썬은 쉬워요
"""
```
<br>

# `슬라이싱`
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

# `문자열 처리 함수`
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

# `문자열 포맷`
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

# `탈출문자`
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

# `리스트 자료형`
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

# `사전 자료형`
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