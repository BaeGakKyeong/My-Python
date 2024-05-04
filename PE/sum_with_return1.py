#두 값의 합을 반환하는 get_sum()함수와 return문의 사용

def get_sum(a, b) :
    result = a + b
    return result   #여기서 result문을 스킵하면, 밑에서 계산한 n1, n2값이 None이 

n1 = get_sum(10, 20)
print('10과 20의 합 :', n1)

n2 = get_sum(100, 200)
print('100과 200의 합 :', n2)