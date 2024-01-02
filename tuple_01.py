t = ("AB", 10, False)
print(t)

t1 = (123)
print(t1) # 튜플 요소가 하나일 때는 정수(int)로 인식한다.

t2 = (123,) # 튜플 요소가 하나일 때는 뒤에 명시적으로 콤마를 붙여 튜플임을 나타낸다.
print(t2)

# 슬라이싱. 튜플은 추가, 삭제, 변경이 불가능

t = (1, 5, 10)

second = t[1] # 5
last = t[-1]  # 10

s = t[1:2]  # 5
s = t[1:]   # 5,10

#Tuple 병합, 반복
a = (1,2)
b = (3,4,5)
c = a + b  #(1,2,3,4,5)

print(c)

d = a * 3
print(d) # (1,2,1,2,1,2)


# 튜플 변수 할당
name = ("John", "Kim")
print(name) # ("John", "Kim")

firstname, lastname = ("John", "Kim")
print(lastname, " , ", firstname) 

