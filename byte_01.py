s = "Hello"
b = s.encode() # encode. 문자열을 바이트로 변환. 접두어 b가 붙는다.
print(b)

# c는 ASCII 코드로 표현된다. 아스키코드가 default. 
for c in b:
    print(c)
    
s2 = b.decode() # 바이트를 문자열로 변환.
print(s2)

# 특정 인코딩 방식을 지정한 경우
x = "안녕".encode("UTF-8")

for c in x:
    print(c) #UTF-8 코드로 표현된다.

x2 = x.decode("UTF-8")
print(x2)