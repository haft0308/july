'''
import random

# 1부터 10 사이의 정수 하나
rand_int = random.randint(1, 10)

# 0 이상 1 미만의 실수
rand_float = random.random()

# 리스트에서 랜덤하게 하나 선택
rand_choice = random.choice(['사과', '바나나', '체리'])

# 리스트를 무작위로 섞기
fruits = ['사과', '바나나', '체리']
random.shuffle(fruits)

'''

# import random
#
# #로또 번호 구하기
#
# #set변수를 선언한다. 객체를 만든다.
# lottoSet = set()
# while len(lottoSet) <=6:  #set의 변수의 갯수가 6개가 될때까지 randint()를 호출한다.
#     randomNum = random.randint(1, 45)
#     lottoSet.add(randomNum)##위에서 구한 수를 set의 변수에 담는다.
#
# print(lottoSet)#로또 숫자 6개 준비됨.
#
# lottoList = list(lottoSet)#set의 요소들을 list에 한꺼번에 담았음. 왜냐면 리스트를 사용해야, 정렬과 같이 값을 갱신하는 동작을 수행할 수 있음.
#                             #6개의 요소를 구하고 나면 그 set변수의 값들을 리스트에 담는다.
# print(lottoList)
#
# #로또번호 정렬하기
#
# def sortOfSelection():#선택정렬 함수
#     # 선택정렬 (첫번째칸의 값과 나머지 요소들과의 크기를 판단해서 자리교환.
#     # 결국, 왼쪽에 가장작은수가 정렬되면서 2중for문의 내부 for에서 j의 시작값이 1개씩 줄어듬.
#     # j의 종료값은 항상 N개까지는 비교해야함.
#     # 선택정렬 정렬.
#     for i in lottoList:  # 12 4 26 45 7 36
#         print(i)  # 12 4 26 45 7 36
#         for j in lottoList:
#             if lottoList[i] > lottoList[j]:
#                 print('선택정렬')
# SUCCESS =-1
# def sortOfBubble(lottoList):
#     #버블정렬 (이웃한 요소 두개의 크기를 비교함. j, j+1 두개를 비교함.
#     # 결과적으로 오른쪽에 가장 큰 값이 배치되면서,
#     #   2중 for문의 내부 for에서 시작점은 j의 시작점은 모두 0이나, 종료되는 위치는 정렬이 하나씩 되면서 줄어듬. N, N-1 과 같이.
#     return SUCCESS
#
#
# sortOfSelection()
# sortOfBubble(lottoList)
#
#
#



for x in range(4):
    if x==2:
        continue
    print(x)


#최종적으로 리스트가 로또번호임.




