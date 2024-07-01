#가변 인자의 활용

def sum_nums(*nums):
    result = 0
    for n in nums :
        result += n
    result / len(nums)
    