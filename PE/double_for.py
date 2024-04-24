#이중 for문을 이용한 구구단의 출력

for x in range(1, 10) :
    for y in range(2, 6) :
        print(y, '*', x, '=', x * y, end = '\t')
    print()
print()

for x in range(1, 10) :
    for y in range(6, 10) :
        print(y, '*', x, '=', x * y, end = '\t')
    print()
    
        