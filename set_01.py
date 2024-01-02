# 중복을 제거하여 중복없는 요소로만 구성된 집합 컬렉션

# 중복제거
myset = {1, 1, 3, 5, 5}
print(myset)

# 리스트를 set으로 변환
mylist = ["A", "A", "B", "B", "B"]
s = set(mylist)
print(s)


# Set에서의 추가 및 삭제
myset = {1, 3, 5}

# 하나만 추가
myset.add(7)
print(myset)

# 여러개 추가
myset.update({4,2,0})
print(myset) # {0,1,2,3,4,5,7} 오름차순으로 정리까지 해준다.

# 하나만 삭제
myset.remove(1)
print(myset)

# 모두 삭제
myset.clear()
print(myset)


## 집합연산
a = {1, 3, 5}
b = {1, 2, 5}

i = a & b # 교집합
# i = a.intersection(b)
print(i)

u = a | b # 합집합
# u = a.union(b)
print(u)

#차집합
d = a - b
# d = a.difference(b)
print(d)
