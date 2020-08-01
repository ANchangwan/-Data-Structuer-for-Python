# # 예제 1(while 문)
# num = int(input('1부터 n까지 합을 구하시오'))
# sum =0
# i = 1
# while i<=num:
#     sum+=i
#     i+=1
# print(sum)

# # 예제 2(for 문)
# n = int(input('1부터 n까지의 정수를 입력해주세요'))
# sum = 0
# for i in range(1,n+1):
#     sum+=i

# print(sum)

# # 예제 3
# print('a부터 b까지의 합을 구합니다.')
# a = int(input('a의 값 : '))
# b = int(input('b의 값 : '))

# if a > b:
#     a,b = b,a
# sum = 0
#  for i in range(a, b+1):
#      sum += i
#  print(sum)

# # 예제 4
# print('a부터 b까지의 합을 구합니다.')
# a = int(input('a의 값 : '))
# b = int(input('b의 값 : '))

# if a > b:
#     a,b = b,a
# sum = 0
# for i in range(a,b+1):
#     if i<b:
#         print(f'{i}+ ',end = '')
#     else:
#         print(f'{i} =', end = '')
#     sum += i

# print(sum)

# 예제 5 (예제 4 개선)

# print('a부터 b까지의 합을 구합니다.')
# a = int(input('a의 값 : '))
# b = int(input('b의 값 : '))

# if a<b:
#     temp = a
#     a = b
#     b = temp

# sum = 0

# for i in range(a, b):
#     print(f'{i}+ ',end = '')
#     sum+=i

# print(f'{b} = ', end ='')
# sum+=b
# print(sum)

# 효율적인 이유는 조건문을 통해서 크거나 같음을 판별할필요도 없고 반복 횟수를 한번 줄이기 때문에 효율적이다.

# 반복 과정에서 조건 파단하기 2

# # 예제 1
# print('반복과정에서 +,-를 반복 출력합니다')
# num = int(input('+,- 를 반복 출력합니다.'))

# for i in range(num):
#     if i%2:
#         print('-',end = '')
#     else:
#         print('+', end = '')
# print()

# 이 코드의 문제점
# 1. for 문을 반복 할때마다 if문을 수행해야한다.
# 2. 상황에 따라 유연하게 수정하기 어렵다.

# 예제2(예제1 개선)

# print('+와 -를 번갈아 가면 출력합니다.')
# num = int(input('몇 개를 출력할까요?'))

# for _ in range(num//2):
#     print('+-',end = '')

# if num%2:
#     print('+', end = '')

# print()

# 예제 3
# 반복 과정에서 조건 판단하기3

# print('*을 출력합니다.')
# countStarNum = int(input('원하는 별의 갯수'))
# lineBreak = int(input('몇 개마다 줄바꿈을 하고 싶은세요?'))

# for i in range(countStarNum):
#     print("*",end = '')
#     if i%lineBreak == lineBreak - 1:
#         print()

# if lineBreak%2:
#     print()

# 예제4
# 예제3 개선

# print('*을 출력합니다.')
# countStarNum2 = int(input('원하는 별의 갯수를 입력해주세요.'))
# lineBreak2 = int(input('원하는 줄 바꿈 갯수를 입력해주세요. '))

# for i in range(countStarNum2//lineBreak2):
#     print('*'*lineBreak2)

# rest  = countStarNum2%lineBreak2
# if rest:
#     print('*'*rest)

# 양수 입력받기
#1부터 n까지의 합을 구하기

# 예제 1

print('1부터 n까지의 정수의 합을 구합니다.')


while True:
    num = int(input('원하는 정수값을 입력해주세요'))
    if num>0:
        break
    else:
        print('정수를 입력해주세요')
        continue


sum = 0
i = 1

for i in range(1,num+1):
    sum+=i
    i+=1

print(f'1부터 {num}까지의 합은 {sum}입니다.')
