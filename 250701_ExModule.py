
# from math import *
# print(pow(2, 3))
# print(pi)

# import math
# print(math.pi)
# print(math.pow(2,4))

# from math import log
# print(math.log(10, 10))

# from 모듈명 import 변수명, 함수명 또는 클래스명
# from math import e as A
# print(A)

import math
import turtle
t = turtle.Turtle()
t.color('red', 'yellow')#선색은 red 채우기 색:노랑

t.begin_fill()

t.forward(200)

# t.left(90)
# t.forward(200)
#
# t.left(90)
# t.forward(200)
#
# t.left(90)
# t.forward(200)

for i in range(3):
    t.left(90)
    t.forward(200)

t.end_fill()

turtle.done()


math.sqrt(2) #<--대각선길이.