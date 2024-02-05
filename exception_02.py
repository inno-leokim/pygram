def calc(values):
    sum = None
    try:
        sum = values[0] + values[1] + values[2]
    except (IndexError, ValueError):
        print('오류발생')
    finally:
        print(sum)

calc([1,2,3,4])
calc([1,2])