a = [] # 빈 리스트 선언

# 리스트 요소는 서로 다른 타입 가능
a = ["AB", 10, False]
x = a[1]
a[1] = "Test" # 두번째 요소 변경
y = a[-1]  #False

print(x) # 10

# 리스트 슬라이싱
a = [1, 3, 5, 7, 10]
x = a[1:3] # 인덱스 1부터 시작, 3번째 요소까지..  [3,5]
x = a[:2]  # 인덱스 0부터 시작, 2번째 요소까지..  [1,3]
x = a[3:]  # 인덱스 3부터 시작, 마지막 요소까지..[7,10]
x = a[:]   # 전체

b=[1,2,3,4,5]
x=a[::2] #세번째 값은 스텝을 의미. 즉, 2칸씩 건너 뛴다는 의미이다. [1,3,5]

c=[1,2,3,4,5]
x=a[::-1] # -1은 역순을 의미. [5,4,3,2,1]

# 리스트 요소 추가, 수정, 삭제
a = ["AB", 10, False]
a.append(21.5) #추가
a[1] = 11 # 변경
del a[2]  # 삭제
print(a)  # ['AB', 11, 21.5]


#리스트 병합과 반복 
a=[1,2]
b=[3,4,5]
c=a+b #병합
print(c)

d=a*3 #반복
print(d)


#리스트 검색
mylist = "This is a book That is a pencil".split() #빈칸 기준으로 split하여 list화
i=mylist.index('book') # i=3  book의 인덱스는 3이다.
n=mylist.count('is')   # n=2  is가 배열중에 2개 있다.

#List Comprehension
list = [n ** 2 for n in range(10) if n % 3 == 0] # n in range(10) => 0부터 9까지
print(list) # 출력: [0,9,36,81]
