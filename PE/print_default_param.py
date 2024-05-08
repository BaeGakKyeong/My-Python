#디폴트 매개변수의 설정

def print_star(n = 1) :
    for _ in range(n) :
        print('**********************')

print_star()    #인자 없이도 잘 작동함
print()
print_star(2)   #인자를 입력하면 디폴트값은 적용되지 않는다.
