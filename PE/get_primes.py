#2부터 100까지 소수 구하기

primes = []     #소수를 담을 리스트 초기화

for n in range(2, 101) :
    is_prime = True     #연역추론, 일단 참이라고 가정한다.
    for num in range(2, n) :    
        if n % num == 0 :
            is_prime = False
    if is_prime :
        primes.append(n)
        
print(primes)
            