# 문자열 클래스 
# 문자열은 기본적으로 유니코드. 
# 한번 설정되면 변경 x(immutable)

s = "ABC"
print(type(s))

# 파이썬에는 C, C# 등에서 존재하는 문자(char) 타입이 존재하지 않는다. 따라서, 위의 예에서 s[1]의 타입이 char가 아닌 문자열 str 타입이 된다.
v = s[1]
print(type(s[1]))

# 문자열을 표현할 때, r'문자열' 과 같이 사용하면, 이는 Escape Sequence를 표현하지 않고 
# Raw String을 직접 사용한다는 것을 의미한다. 
# 예를 들어, 윈도우즈에서 파일경로를 간략히 표현하기 위해 아래와 같이 Raw String 표현을 사용할 수 있다.
path = r'C:\Temp\test.cvc'
print(path)

##
# str 메서드(join, split, partition)
##

# join
s = ','.join(['가나', '다라', '마바'])
print(s)

s = ''.join(['가나', '다라', '마바'])
print(s)

# split
items = '가나,다라,마바'.split(',')
print(items)

# partition
# partition() 메서드는 문자열을 partition() 메서드의 첫번째 파라미터로 분리하여 
# 그 앞부분(prefix), partition 분리자(separator), 뒷부분 (suffix) 등 3개의 값을 Tuple로 리턴한다. 
# 아래 예제는 Dash (-) 로 문자열을 분리하여 3개의 값을 리턴하는 코드이다. 
# 일반적으로 separator는 사용하지 않아서 _ 를 사용하였다.

departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)


# format
# {}안의 필드들을 format()의 파라미터들로 치환

# 위치를 기준으로 한 포맷팅. 파라미터들의 순서대로 치환 
s = "Name: {0}, Age: {1}".format("강정수", 30)
print(s)

# 필드명을 기준으로 한 포맷팅
s = "Name: {name}, Age: {age}".format(name="강정수", age=30)
print(s)

# object의 키 또는 인덱스를 사용하여 포맷팅
area = (10, 20)
s = "width: {x[0]}, height: {x[1]}".format(x = area)
print(s)


