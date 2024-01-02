#literal로 dic 생성
scores = { "철수": 90, "민수": 85, "영희": 80} 
v = scores["민수"]
scores["민수"] = 88
print(v)


# tuple list로부터 dic 생성
persons = [('김기수', 30),('홍대길', 35),('강찬수', 25)]
mydict = dict(persons)

age = mydict["홍대길"]
print(age)

#key=value 파라미터로부터 dict 생성
scores = dict(a=80, b=90, c=85)
print(scores['b'])


#추가, 수정, 삭제, 읽기
scores = {"철수": 90, "민수": 85, "영희": 80}
scores["민수"] = 88   # 수정
scores["길동"] = 95   # 추가
del scores["영희"]
print(scores)

scores = {"철수": 90, "민수": 85, "영희": 80}

for key in scores:
    val = scores[key]
    print("%s : %d" % (key, val))


# dict 메서드 
scores = {"철수": 90, "민수": 85, "영희": 80}

#keys
keys = scores.keys()
for k in keys:
    print(k)

#values
values = scores.values()
for v in values:
    print(v)

#dict_items
scores={"철수": 90, "민수": 85, "영희": 80}

items = scores.items()
print(items) # dict_items([('철수', 90), ('민수', 85), ('영희', 80)])

# dict_itmes를 list로 변환
itemList = list(items)
print(itemList) # [('철수', 90), ('민수', 85), ('영희', 80)]

scores={"철수": 90, "민수": 85, "영희": 80}
v = scores.get("민수") #85
v = scores.get("길동") #None    => get을 쓰는 것이 좋다. 
# v = scores["길동"] # Error 발생

if "길동" in scores:
    print(scores["길동"])


#clear
scores.clear()
print(scores)

#update
persons=[('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
mydict = dict(persons)

mydict.update({'홍대길': 33, '강찬수': 26})
print(mydict)