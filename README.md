# 숫자 자료형
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

# 문자열 자료형

```python
print('Python') # Python
print("Python") # Python
print("Python"*3) # PythonPythonPython
```
<br>

# boolean 자료형

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

# 변수

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

# 주석
```python
# 한 줄 주석

''' 여러
줄
주석 '''
```
<br>

# 연산자
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

# 숫자 처리 함수
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

# 랜덤 함수
```python
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성

print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(randrange(1,10) # 1 ~ 10 미만의 임의의 값 생성

print(randint(1,10)) # 1 ~ 10 이하의 임의의 값 생성
```