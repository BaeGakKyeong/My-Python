#이중 for문을 활용한 패턴 출력

#내 풀이
for i in range(0, 7) :
    for j in range(0, i) :
        print(end = ' ')
    print('#')
    
#교재에 제시된 풀이
for i in range(7) :
    st = ''
    for j in range(i) :
        st += ' '
    print(st + '#')
    
#내 풀이에는 print()문이, 교재의 풀이에는 변수가 각각 하나씩 많기 때문에 효윯성은 같다.

#교재의 다른 풀이
for i in range(7) :
    print(' ' * i + '#')    #문자열과 변수는 연산할 수 있다. 

#for문도 하나고, 변수도 하나 뿐이기 때문에 코드의 효율성과 가독성이 모두 좋다. 

print()
print()

#LAB 3-9 : 패턴 출력 응용
for i in range(6, -1, -1) :
    for j in range(0, i) :
        print(end = ' ')
    print('#')
print()

for i in range(6, -1, -1) :
    print(' ' * i + '#')