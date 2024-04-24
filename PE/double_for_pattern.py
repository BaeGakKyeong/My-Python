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
    
#내 주관으로는, 내 코드의 가독성이 더 좋다고 생각한다. 내 풀이에는 print()문이, 교재의 풀이에는 변수가 각각 하나씩 많기 때문에 효윯성은 같다.