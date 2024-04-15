#P.106 Q.2.8(수정) 밑과 지수를 입력받고, 밑은 1씩 커지고 지수는 유지, 그 결과를 출력하는 프로그램

print('밑과 지수를 입력받아 그 결과를 출력하는 프로그램')

base = int(input('밑을 입력하시오 : '))
square = int(input('지수를 입력하시오 : '))     #int()가 없으면 연산 실행 불가

print('밑 \t\t 지수 \t\t 밑**지수')
print(base, '\t\t', square, '\t\t', base ** square)

base += 1
print(base, '\t\t', square, '\t\t', base ** square)

base += 1
print(base, '\t\t', square, '\t\t', base ** square)

base += 1
print(base, '\t\t', square, '\t\t', base ** square)

base += 1
print(base, '\t\t', square, '\t\t', base ** square)

