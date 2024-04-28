#양수 n을 입력받아 1부터 n까지의 합을 구하는 프로그램

num = 0
while num <= 1 :
    num = int(input('자연수를 입력하시오 : '))

s = 0
for i in range(1, num + 1, 1):
    s += i
    
print('1부터 {}까지의 합은 : {}' .format(num, s))
