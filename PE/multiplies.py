#다수의 결과를 반환하는 함수 만들기

def multiplies(n, m) :
    for i in range(1, m + 1, 1) :
        print(n * i, end = ' ')
        
multiplies(3, 4)