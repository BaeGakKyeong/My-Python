#세 수를 입력받아 근을 구하는 프로그램

def QF(a, b, c) :
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print('{}x^2 + {}x + {}의 해는 {} 또는 {}' .format(a, b, c, r1, r2))

print('ax^2 + bx + c')    

i = 0
while i == 0 :
    i = float(input('0이 아닌 a값을 입력하시오 : '))
j = float(input('b갑을 입력하시오 : '))
k = float(input('c값을 입력하시오 : '))

QF(i, j, k)