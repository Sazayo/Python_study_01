# 파이썬에서의 자료형(Data-type)
# int 형을 출력해봄
print(type(17))
# float 형을 출력해봄
print(type(10.7777))
# str 형을 출력해봄
print(type("안녕하세요"))

# 반지름이 r인 구의 부피는 4/3 * PI * r의 세제곱 공식
# 반지름이 5인 구의 부피를 계산하는 프로그램
from math import *
r = 5.0
# volume = 4.0/3.0 * pi * r**3
volume = 4.0/3.0 * pi * pow(r, 3)
print("구의 부피 : " + "%s" % volume)
print("구의 부피 : " + str(volume))
print("구의 부피 : ", volume)
print(pi)

# 구의 겉넓이 공식 : 4 * pi * r의 제곱
outer_area = 4 * pi * pow(r, 2)
print("구의 겉넓이 : " + "%s" % outer_area)
print("구의 겉넓이 : " + str(outer_area))
print("구의 겉넓이 : ", outer_area)

# 문자열 + float 는 타입이 일치가 안되어 문자열을 생성할 수 없음
# 해결방안은 문자열 즉 숫자로 변환이 되지 않는 문자열을 숫자로 변환해주는 것


