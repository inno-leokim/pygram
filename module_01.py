## math 전체 라이브러리를 호출
# import math 

# n = math.factorial(5)
# print(n)

## factorial 함수만 import
# from math import factorial

# n = factorial(5) / factorial(3)

## 여러 함수를 import
# from math import (factorial, acos)
# n = factorial(3) + acos(1)

## 모든 함수를 import
# from math import *
# n = sqrt(5) + fabs(-12.5)

## 함수에 alias 사용
from math import factorial as f 
n = f(5) / f(3)




