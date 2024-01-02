def sum(a,b):
    s = a + b
    return s

total = sum(4, 7)
print(total)


def f(i, mylist):
    #mylist는 list
    i = i + 1
    mylist.append(0) #list는 call by reference
    
k = 10
m = [1, 2, 3]

f(k,m)
print(k, m)
    
# default 파라미터(parameter)
def calc(i, j, factor=2):
    return i * j * factor

result = calc(10,20)
print(result)


# Named Parameter: 파라미터 네임을 맞춰주면 순서를 변경해도 파라미터 전달이 가능하다.
def report(name, age, score):
    print(name, score)
    
report(age=10, name="kim", score=80)


# 가변길이 파라미터 
def total(*numbers):
    tot = 0
    for n in numbers:
        tot += n
    return tot

t = total(1,2)
print(t)
t = total(1,5,2,6)
print(t)

# 리턴값
def calc(*numbers):
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n 
    return count, tot 

count, sum = calc(1,5,2,6)
print(count, sum)