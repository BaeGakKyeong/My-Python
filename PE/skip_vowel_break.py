#break를 사용하여 모응이 나타나면 반복문을 종료하는 기능

st = 'programming'
for ch in st :
    if ch in ['a', 'e', 'i', 'o', 'u'] :
        break
    print(ch)
    
print('the end')