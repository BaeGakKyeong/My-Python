#두개의 값을 튜플로 반환하는 방법과 전달하는 방법

def get_root(a, b, c) :
    r1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return r1, r2

result1, result2 = get_root(1, 2, -8)
print('해는 {}또는 {}입니다' .format(result1, result2))