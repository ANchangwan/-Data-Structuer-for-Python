n = int(input('저장할 정수갯수를 입력하세요 : '))
a = [None] * n                  # 입력바은 값을 저장하는 배열

cnt = 0                         # 정수를 입력받은 개수

while True:
    a[cnt%n] = int(input(f'{cnt + 1}번째 정수를 입력하세요 : '))
    cnt+=1

    retry = input(f'계속할까요? (y...(yes)/(n...No))')
    if retry in {'N','n'}:
        break

i = cnt - n
if i <0 : i =0

while i<cnt:
    print(f'{i + 1}번째 = {a[i%n]')
    i+=1