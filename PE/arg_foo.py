#가변 인자를 가지는 함수에서 len()함수의 활용

def foo(*args):
    print('인자들의 개수:', len(args))
    print('인자들 :', args)
    
foo(10, 20, 30)