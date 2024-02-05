# list comprehension은 []로 시작

oldlist = [1, 2, 'A', False, 3]
newlist = [i*i for i in oldlist if type(i) == int]

print(newlist)


# set comprehension은 {}로 시작
oldlist = [1,1,2,3,3,4]
newlist = {i*i for i in oldlist }

print(newlist)


# dictionary comprehension은 {key:val} 이 포함되어야 한다.
id_name = {1: '박진수', 2: '강만진', 3: '홍수정'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)


def isodd(val):
    return val % 2 == 1

mydict = {x:x*x for x in range(101) if isodd(x)}
print(mydict)    

