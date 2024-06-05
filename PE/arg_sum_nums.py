#가변 인자를 가지는 함수를 이용한 합계 구하기

def sum_nums(*numbers):
    result = 0
    for n in numbers :
        result += n
    return result

print(sum_nums(10, 20, 30))
print(sum_nums(10, 20, 30, 40, 50))


