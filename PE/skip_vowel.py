#continue를 사용하여 모음일 경우 출력을 건너뛰는 경우

st = 'programming'

for ch in st :
    if ch in ['a', 'i', 'o', 'u', 'e']:
        continue
    print(ch)
    
print('the end')