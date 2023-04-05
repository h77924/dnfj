#import random

#print(random.randint(0,10000))

#from random import randint
#print(randint(0,10000))

#놀이동산 탑승 문제
#총 정원 4명
#정원이 차면, 놀이기구 시작
#조건 키 150 이상만 탈수 있음
#사람들한테 키를 물어보고, 탑승시키시오.
#150이상 4명이 되면 놀이기구를 시작

key = 0
while True:
    key = input("키가 몇이에요")
    if key > 150 :
        print("놀이기구에 탑승하시오")
    elif key < 150 : 
        print("놀이기구를 못탑니다. 돌아가시오")