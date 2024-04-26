#그 유명하다는 별찍기 문제

j = 4
for i in range(1, 10, 2) :
    print(' ' * j + '*' * i)
    j -= 1
    
#이중 for문을 이용한 별찍기

st = '*'
for i in range(5) :     #[0, 1, 2, 3, 4]
    for j in range(4-i, 0, -1) :
        print(end = ' ')
    print(st)
    st += '**'
    
#교재에서 제시한 풀이

n = 5
for i in range(n) :
    for j in range(n - (i + 1)) :
        print(' ', end = '')
    for j in range(2 * i + 1) :
        print('+', end = '')
    print()