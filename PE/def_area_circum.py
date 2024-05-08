#원의 면적과 둘레를 반환하는 함수

def circle_area_circum(r) :
    a = 3.14 * r ** 2
    c = 3.14 * 2 * r
    return a, c

area, circum = circle_area_circum(10)
print('반지름이 10인 원의 넓이 : {}, 둘레 : {}'.format(area, circum))