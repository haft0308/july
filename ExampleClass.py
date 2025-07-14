class Iot:
    def __init__(self, department):
        self.department = department

    def __str__(self):
        list = [
                    "Iot department: " + self.department +'\n',
                    f"Iot department: {self.department}\n" ,
                    "department {}\n".format(self.department),
                ]
        return list[0] + list[1]+list[2]

    def add(self, num1, num2):
        return num1 + num2

    #minus메소드 추가
    #mul메소드 추가.


iot = Iot("bukbu")
print(iot)

result = iot.add(1,2)
print(result)
result = iot.minus(2, 1)
print(result)
result = iot.mul(2,2)


'''
list = List()
list.append(1)

list2 = [10, 20, 30, 40]
list[0] = 100

myTuple = tuple();
myTuple2 = (5, 4, 3, 2, 1)
myTuple2[0] = 10 # 안됨. 튜플은 한번 할당하면 더이상 값을 갱신할수 없다.

myDict = { "새우깡":500, "감자깡":1000, "먹태":300}
print(str(myDict['새우깡']))

'''


