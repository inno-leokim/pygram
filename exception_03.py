# 에러무시 에러생성

def calc(values):
    sum = None
    try:
        sum = values[0] + values[1] + values[2]
    except(IndexError, ValueError):
        pass #해당 오류 발생 시 무시하고 패스한다!
    finally:
        print(sum)

calc([1, 2]) #결과는 None. 에러는 발생하지 않는다.

# 에러발생은 raise 명령어로 한다.
def calc02(value):
    total = value
    if total < 0:
        raise Exception('Total Error')

calc02(-1) # 에러 발생