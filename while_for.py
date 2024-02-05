# while
i=1
while i<=10:
    print(i)
    i += 1

# for
sum=0
for i in range(10):
    sum += i
print(sum)

list = ["This", "is", "a", "book"]
for s in list:
    print(s)

# break / continue    
i = 0
sum = 0
while True:
    i += 1
    if i == 5:
        continue
    if i >10:
        break
    sum += i

print(sum)

# range (index, 실제순서)
# range(3)	    Stop	            0, 1, 2
# range(3,6)	Start, Stop	        3, 4, 5
# range(2,11,2)	Start, Stop, Step	2, 4, 6, 8, 10

numbers = range(2, 11, 2)

for x in numbers:
    print(x)
    
for i in range(10):
    print("Hello")