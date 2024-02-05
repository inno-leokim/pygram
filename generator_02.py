# Generator Expression
g = (n*n for n in range(1001))

print(type(g))

#리스트로 일괄 변환시
# mylist = list(g)

# 10개 출력
for i in range(10):
    value = next(g)
    print(value)

print("======#######======")

# 앞서 출력한 10개 이후를 출력
for x in g:
    print(x)
    