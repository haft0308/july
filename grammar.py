# '''
# score1 = int(input('첫번째 사람의 점수를 입력하세요'))
# score2 = int(input('두번째 사람의 점수를 입력하세요'))
#
# if score1 > score2:
#     print('첫번째 사람이 1등')
#
# else:
#     print('첫번째 사람이 2등')
#
# print("1등은 쉬기")
# print("2등은 설거지하기")
#
#
#
# scoreList = []
# '''
#
# gugudan=[]
# for i in range(10):
#     gugudan.append(i+1)
#
# for i in gugudan:
#     print(i)
# gugudan[0] = 0
#
# for i in gugudan:
#     print(i)
# # i++
# # i=i+1
# #
# for i in range(2):
#     # scoreList.append(int(input(f'{i+1}사람의 점수를 입력하세요')))
# #
# # print(scoreList)
# #
# # #grade_1 = scoreList[0]
# # if scoreList[0] > scoreList[1]:
# #     #grade_1 = scoreList[0]
# #     print(scoreList[0], '이 1등입니다')
# #     print(f"{scoreList[0]} 이 1등입니다")  # 서식 문자열.
# #     print(f"{scoreList[1]} 이 2등입니다")  # 서식 문자열.
# # else:
# #     #grade_1 = scoreList[1]
# #     print(scoreList[1], '이 1등입니다')
# #     print(f"{scoreList[0]} 이 2등입니다")  # 서식 문자열.
# #
# # print("\n")
# # for i in scoreList:
# #     print(i)
# #
# # scoreList[0] = 0
# # for i in scoreList:
# #     print(i)
#
# gugu = (60, 70, 80, 90)#튜틀
#
# for i in gugu:
#     print(i)
# # gugu[0]=100
#
# score = { '승준':60, '은희':10}
# print(score)
#
# print(score['은희'])
#
# score['은희']=100
# print(score)
#





#딕셔너리 자료형 사용하기
# table = { 'A101':'강신우','A102':'봉준호', 'A103':'김민호', 'A104':'문소리', 'A105':'박문수' }
# print(table)
# print(table['A104'])
#
# table['A105'] = '둘리'
# print(table['A105'])
#
# for i in table:
#     print(table[i])

ex = {'A101 강신우':10, 'A102 봉준호':30}#'A101 강신우'의 키값을 변경하고 싶으나,
                                        #키값은 변경할 수 없다.
                                        #키값을 새로 넣어주고, 기존의 키값은 삭제하자
ex['A101'] =ex['A101 강신우']
del ex['A101 강신우']
print(ex)

ex2 = []        #리스트 변수 사용하기
ex2.append('김밥')
ex2.append('떡볶이')
ex2[0] = '오뎅'


#튜플변수 사용하기
ex3 = ('최지원', '김민제', '유하성', '이건희', '임소은', '강건', '이정훈')
print(ex3[3])
# ex3[3] = '고희선'#안됨. 튜플은 만들떄 값 한번만 할당함.

for item in ex3:
    print(item)
'''
#최지원, 김민제, 유하성(V)
for i in range(10):
for i in range(0,3):#0, 1, 2
#김민제, 이건희, 강건(V)
for i in range(0, 3, 2):
#i%2 == 0
for i in range(6, 4, -1):
#이정훈, 강건, 임소은(V)
'''
#369게임 완성하기
# for i in range(0,100,1):
#     # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
#     #     짝    짝    짝       짝  짝    짝        짝       짝    짝 짝
#     if (i % 3 == 0 ) and (i%5 == 0) or (i<0):
#         print('짝');
#     else:
#         print(i);

#10번만 입력받자.
cnt=0;
while ( True ):
    score = int(input('점수를 입력하세요'))
    #score의 값만큼 *를 그래프처럼 오른쪽으로 그려주세요
    # {score:3} **********
    # 100 '*'*100
    #for를 사용해서 *를 그리세요
    cnt=cnt+1
    if cnt == 10:
        break
    else:
        pass # 아무것도 하지 않고 넘어간다는 의미로 pass를 명시함.
             # 뭔가써야할 자리에 임시로 비워둘때, 표기.


mySet = set([5, 2, 1, 2, 3, 4, 5])
print(mySet)
print(len(mySet))
print(mySet)

myList = list(mySet)
print(myList)