#0503

'''
작성법
def function_name(input1, input2, input3) :
    수행문1,
    수행문2

함수 이름 - addthree
기능 : 3을 더함
input : 숫자 1개
output : 숫자 1개, input 숫자에다가 3을 더한것을 내보냄.
def addthree(num) :
    return num + 3

result = addthree(100) # result = 103
print(addthree(100))
print(result)


def printaddthree(num) :
    print(num + 3)

printaddthree(100)
'''

#fuction 작성
#fuction1 - 사람 이름 2개를 입력받아서
# 안녕!사람1, 안녕 사람2 출력
#fuction1 이름- hello
# parameter - name1, name2
#결과 - print(hello name1, hello name2)
'''
def hello(name1="배진호", name2="주재석"):
    print("hello ", name1)
    print("hello ", name2)

hello("배","주") # 배,주 출력
hello() #기본값 출력(배진호,주재석)
'''

#fuction2 작성
#fuction2 - 숫자 두개 입력받아서,
#           두개의 합을 return하는 함수를 정의하라
#parameter - num1, num2
#결과 - return num1 + num2
'''
def mysum(num1, num2):
    return num1 + num2

result = mysum(100, 200)
print(result) #300출력
'''

#function이름은 mysum2
#인자는 몇개가 들어올지 모름
#결과 - 모든 인자의 합을 return
'''
def mysum2(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    return result

print(mysum2(1,1,1,1,1,1,1,1,1,1))
#mysum2(1,2,3,4,56,7,8,9,9,9)
'''

'''
#리스트를 호출하고 싶을때
lst1 = [10,10,10,10,10,10,10,10,10,10] 
lst2 = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

print(mysum2(*lst1))
print(mysum2(*lst2))
'''

#key value pair
#cafe function
#메뉴 = 가격을 출력해주는 function을 만들자.
'''
def cafe(**keyvalue):
    #수행문 menu와 가격을 출력하라.
    for key in keyvalue: #아메, 라떼, 핫초코
        print(key, " ", keyvalue[key]) # 아메, 2000

cafe(아메=2000, 라떼=3000, 핫초코=5000)
print("=================")
cafe(아메=2000, 라떼=3000)
print("=================")
cafe(아메=2000)
print("=================")
menu = {"아메리카노":3000, "마카롱":3000, "핫초코":3000} #딕셔너리 호출하고 싶을때
cafe(**menu)
'''

#####################3
#Lambda function - 람다 함수
#짧게 간결하게 쓰고 싶어서 개발된 function
#function 이름 짓기 싫을때
# 수행문이 한줄이다.
'''
def addthree(num) :
    return num + 3
print(addthree(100))

print((lambda num : num + 3)(100)) # 람다 사용법 103
'''

#1) 숫자 입력받아서, 10을 곱해서 renturn 함수 - Lamdba로 만들어보자. 호출까지 하시오
'''
def multtien(n):
    return n*10
print(multtien(20))

print((lambda n: n * 10)(20))
'''

#2) 숫자를 두개 입력, 두개를 곱해서 renturn - Lambda 호출까지 하시오 
'''
def multip(n1, n2):
    return n1* n2
print(multip(3,5))

print((lambda n1,n2: n1*n2)(3,5))
'''

#map, filter
'''
map(function,list)
map(function,[1,2,3,4,5])
[function(1),function(2),function(3), ..., function(5) ]
'''
'''
def addthree(num) :
    return num + 3

print(list(map(addthree, [10,20,30,40,50])))

print(list(map(lambda x : x+3, [10,20,30,40,50])))
'''

#1
#[1,2,3,4,5]
#5배를 하고, 10을 더해서 결과를 list로 출력하시오

#1)function
'''
llist = [1,2,3,4,5]
def calculate(num):
    return num *5+10

print(list(map(calculate, llist)))
'''
#2)lamdba
'''
llist = [1,2,3,4,5]
print(list(map( lambda num: num*5+10, llist)))
'''

#2
#lst10=[10,20,30,40,50]
#lst11=[1,2,3,4,5]
#두개의 list를 하나씩 뽑아서, 두개를 더해서 하나의 리스트로 만들어라
#결과값 [11,22,33,44,55]

#1)function
# 두개의 값을 입력으로 받아서, 그 합을 구하는 function
'''
lst10=[10,20,30,40,50]
lst11=[1,2,3,4,5]
def mysum(n1, n2):
    return n1+n2

print(list(map(mysum,lst10, lst11)))
'''
#2)lambda
'''
lst10=[10,20,30,40,50]
lst11=[1,2,3,4,5]
print(list(map(lambda n1,n2 : n1+n2,lst10, lst11)))
'''

#filter
# 조건을 만족하는가? 만족하면 결과물에 포함, 만족하지 않으면 포함 x
#map이랑 마찬가지로, 입력 리스트로 받아서, 그걸 결과로 나타냄.
#map(functiom, list)
#filter(function, list)
def positive(x):
    if x > 0 :
        return True
    else:
        return False

def positive2(x):
    return x>0
 

print(list(filter(positive, [10,-2,3,-5,9])))
print(list(filter(lambda x : x>0 , [10,-2,3,-5,9])))

