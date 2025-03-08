
# 1. 문자열 포맷팅
  # 특정 문자열 안에 어떤 값을 삽입할 때 사용
  # 문자열 포맷팅 연산자 : %

# 2. 문자열 포맷 코드
 # %s : 문자열(String)
name = "Juyeon"
gender = "female"
print(
"Hi, I'm %s.\n"
"I'm %s." %(name,gender))

# %d : 정수(Integer)
age = 22
height = 169
weight = 53
print(
"I'm %d years old.\n"
"height is %d cm, weight is %d kg." % (age, height, weight))

# %f : 실수(Float)
Pi = 3.1415926535
print("Pi is %.2f." % Pi)

# 위의 방법은 구버전 파이썬에서 사용하는 방법.

# f문자열 포매팅
a = f'I am {name}.'
print(a)