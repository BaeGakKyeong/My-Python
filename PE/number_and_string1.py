#문자열과 정수의 덧셈연산

my_age = 22
my_height = '177'

my_age = my_age + 1
my_height = my_height + 1

print(my_age, my_height)

"""
위의 코드에서, my_age식별자에 정수를 더하는 데에는 문제가 없지만,
my_height식별자에 정수를 더하는 데 문제가 발생한다.
그 이유는 문자열 자료형을 리터럴로 가지는 my_height식별자에 정수를 더하는 것이 불가능하기 때문이다.
"""

