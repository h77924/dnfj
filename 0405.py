#문자열
'''
str = "파이썬수업 씨수업 자바수업 파이썬 수업 파이썬 수업"
str2 = "파이썬수업 씨수업 자바수업 파이썬 수업 파이썬 수업"


#format
#3+4=7

print(3, "+", 4,"=",7)
f1 = "{} + {} = {}".format(3,4,3+4)
f2 = "{0} + {1} = {2}, {2}, {2}, {2} ".format(3,4,3+4)
f3 = "{0:d} + {1:f} = {2:f}, {2:f}, {2:}, {2:} ".format(3,4.0,3+4.0)
f4 = "{0:10d} + {1:10f} = {2:10.3f}".format(3,4.0,3+4.0)
print(f4)


#join
#print("**".join(str))


#split
#print(str.split())
print(str2.split(","))
print(str2.split("업"))


#replace
print(str.replace("파이썬","자바",3))

#count
print(str.count("파이썬"))

#find, index
print("find :", str.find("씨"), "index :", str.index("씨"))
print(str.find("AI"))
print(str.index("AI"))


#bool
print(type(True), type(False))
a = "hello"
print(bool("helow"), bool("hi"), bool(3), bool(1.2), bool(-2))
print(bool(""), bool(0))
print(int(True), int(False), str(True))
'''

'''
# 조건문
h = 9
if h < 12 :
    print("오전", h, "가 12보다 작다")

elif h < 18:
    print("오후", h, "가 12보다 크고 18보다 작아요")

else :
    print("오후", h, "가 18보다 크다")
    '''
'''

lunch = input("점심 먹을래?")
if lunch == "yes" :
    print("점심을 먹고 싶군요")
    cafeteria = input("학식?")
    if cafeteria == "yes" :
        print("8호관 1층으로")
    else :
           print("학식을 싫어하는 군요")
           subway = input("Subway?")
           if subway =="yes" :
               print("8호관 1층으로 고고")
           else :
               print("subway를 싫어하는 군요.")
else :
       print("밥먹기 싫군요")
       '''
'''
#fot, while
#for i in 10,25,32,4635,546,5314 :
    #print("i :", i)

for i in range(3,21654,3) :
    print("i :", i)

#for i in range(20) :
    #print("i :", i)


#1부터 10까지 합을 구하시오
#2가지 방법으로, range도 쓰고, 그냥 명시도 하고

sum = 0
for i in 1,2,3,4,5,6,7,8,9,10 :
    sum = sum+i
    print(i,"번째 loop 입니다","sum", sum, "입니다.")

print("range를 사용")
sum = 0
for i in range(1,11,1) :
    sum += i
    print(i,"번쨰 loop : sum은",sum, "sum입니다.")
else :
    print("else안의 문구 : for문이 잘 종료됨")

print("완전 바깥. else밖의 문구 : for 문이 종료됨.")
'''

#sum , 0부터10까지 숫자를 찍고 sum을 구할것임.
'''
sum = 0
n=0
while n<11 :
    #print("n : ",n)
    sum += n
    print(n,"번쨰 sum :", sum)
    #print(n, end=" ",)
    n += 1
print("while 밖에서의 sum의 값", sum)

while 0:
    print("실행이 되지 않음")

print("while 0 다음 줄입니다.")
'''


#break continue
# 단어 입력을 무한 루프로 받는다.
#그 글자를 3번 써줌
#exit" > 루프를 끝내고 종료
#"apple" > 3번 안쓰고 그냥 다시 단어 입력을 받음.
'''
while True :
    word = input("단어를 입력하세요")
    if word == "exit" :
        print("넌 exit를 입력했다. break를 만난다.")
        break
        print("break 뒤의 문장")
    elif word == "apple" :
        print("넌 apple를 입력했다. continue를 만난다.")
        continue
        print("continue뒤의 문장")
    else:
        for i in range(3):
            print(word, end=' ')
        print("해당 단어 끝")

    print("apple을 넣으면 이걸 절대 볼수 없음.")
'''

