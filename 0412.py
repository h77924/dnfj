#0412
#자료형 - 리스트, 튜플, 닥셔너리, 집합
#"김밥","떡볶이", "돈까스"

'''
리스트
["김밥","떡볶이", "돈까스"]
튜플
("김밥","떡볶이", "돈까스")

딕셔너리 - 사전 apple - 동그란 빨간 과일
{k1:v1, k2:v2}
address = {"홍길동":"구로구", "김길동":"부천", "김철수" : "인천"}
'''

["김밥","떡볶이", "돈까스","칼국수"]
#1. 빈 리스트를 만들어서, 하나씩 원소를 추가 하는 방식
'''
lst = []
#print(type(lst))
lst.append("김밥")
lst.append("햄")
lst.append("탕수육")
lst.append("탕")
#print(lst)
lst.append("파스타")
#print(lst)
lst.insert(0,"학식")
#print(lst)
lst.append("햄")
lst.insert(0,"써브웨이")
lst.append("탕")
lst.append("햄")
lst.append("탕")
#print(lst)
'''
#print("list에서 3번째에 있는 값입니다.:",lst[2])

''''
#점심메뉴 출력
for i in range(len(lst)):
    print(lst[i])

#점심메뉴 출력2
for item in lst :
        print(item)


print(lst)
print('lst.count("탕")',lst.count("탕"),lst.index("탕"))

'''


'''
#slicing
lst = ["써브웨이","학식","김밥", "햄","감튀","탕수육","파스타","햄버거","탕","감자","고구마"]
print(lst[::])#전체
print(lst[0:len(lst):1])#전체
print(lst[0:8:2])#써브웨이,김밥,감튀,파스타 0~7 까지 2칸씩 뛰어넘기
print(lst[3:7:1])#햄,감튀,탕수육,파스타 3~6까지 1칸씩 뛰어넘기
print(lst[::-1])#써브웨이 거꾸로
print(lst[0:6:3])#써브웨이, 햄 0~5까지 3칸씩 뛰어넘기
'''

#lst = ["김밥","햄버거","감튀","탕"]
'''
print(lst)

lst.append("김밥")
lst.append("김밥")
print(lst)

lst.remove("김밥")
lst.remove("김밥")
print(lst)


lst.append("+1커피")


item1="커피"
if item1 in lst:
    lst.remove(item1)
    print("커피 존재함",lst)

print("커피존재안함", lst)
'''
'''
print(lst)
print(lst.pop())
print(lst)

print(lst.pop())
print(lst)

print(lst.pop(0))
print(lst)
'''

'''
print(lst)
dessert = ["케잌","커피","우유","와플"]
print(dessert)
lst.extend(dessert)
'''
'''
print(lst)
#print(lst.extend(dessert))
'''
'''
x = "15"
print(type(x))
print(x+"1")
print(x+1)
print(int(x)+1)
print(type(x))
'''
'''
l1 = ["apple","orange","banana","kiwi","mango"]
print(l1)

print(sorted(l1))
print(l1)

print("l1.sort 실핼")
l1.sort()
print(l1)

l1.reverse()
print(l1)

del l1
print(l1)
'''
'''
l2 = [0,1,2,3,4,5,6,7,8,9,10]
print("l2:",l2)

l3 = []
for i in range(11) : 
     l3.append(i)
print("l3 :", l3)


l4 = [i for i in range(11)]
print("l4 :",l4)
'''
'''
#0-10까지의 숫자의 제곱을 리스트에 넣어라
l5 = []
for i in range(11) :
    l5.append(i**2)


l5 = [i**2 for i in range(11)]
print(l5) 



#0-10까지의 숫자의 3배수 리스트에 넣어라
l6 = [i*3 for i in range(11)]
print(l6) 


#hello를 10번 넣어라
l7 = []
for i in range(10):
    l7.append("hello")
print(l7)

l7 = ["hello" for i in range(10)]
print(l7)

#0-10까지의 짝수들의 제곱을 리스트에 넣으시오 0,4,16..100
l8 = []

for i in range(11):
    if i % 2 ==0 :
        l8.append(i**2)
print(l8)

l9 = [i**2 for i in range(11) if i % 2 ==0 ]
print(l8)

l80 = []

for i in range(11):
    if i % 2 == 0 :
        if i % 3== 0 :
            l80.append(i**2)

print(l80)

l91 = [i**2 for i in range(11) if i % 2 ==0 if i % 3== 0 ]
print(l91)
'''


#list를 복사
a = [0,4,16,36,64,100]
b = a
print("a :", a)
print("b :", b)

a.pop()

print("a :", a)
print("b :", b)

print("a is b", a is b)
print("=====after b.appeend(333)")
b.append("333")
print("a :",a)
print("b :", b)

#deep copy
#c = a[:]
#c = a.copy()
c = list(a)
print("a is c : ",a is c)
print("deep copy")
print("a :",a)
print("c :",c)

a.pop()
print("after a.pop()")
print("a :",a)
print("b :",b)
print("c :",c)

c.append(555)
print("after c.append(555)")
print("a :",a)
print("b :",b)
print("c :",c)

