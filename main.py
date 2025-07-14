print('iot')
print("고길동")

try:
    score = input('시험성적을 입력하세요')
    print(score)
    print(type(score))
    scoreInt = int(score)
    print(scoreInt)
    print(type(scoreInt))

    if scoreInt > 80:
        print('합격!')
    elif scoreInt > 50:
        print("재시험!")
    else:
        print("불합격!")
#except ValueError:
except ValueError as e:
    print("유효하지 않은 값임!", e)

