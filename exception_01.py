def calc(values):
    sum = None
    
    try:
        sum = values[0] + values[1] + values[2]
    except IndexError as err:
        print('인덱스 에러')
    except Exception as err:
        print(str(err))
    else:
        print('에러없음')
    finally:
        print(sum)

calc([1,2,3,4])
calc([1,2]) #에러 발생