#for문을 이용한 팩토리얼 계산

n = int(input('자연수를 입력하시오 : '))
total = 1

for i in range(1,n + 1) :
    total *= i
    
print('{}! = {}' .format(n, total))