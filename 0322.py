#2023-3-22
'''이것은
여러줄짜리
주석입니다.
'''
print("오늘은 파이썬 수업니다.")
print('hello')
print(type("오늘은 파이썬 수업니다."))

print(2)
print(type(2))
print(5.5)

print("hello" + "python")
print("213호" * 3)


print("hello", "hi", "213호")
print("hello", "hello", 213, "" ,11111)
print("hello" + "python")

print(1,2,-5,3.14,2.71828)
print("Hi", "python")

print("23000원은", "5000원 ?개", "1000원?개")
print("5000원",23000 // 5000, "개")
print("1000원",(23000%5000) // 1000, "개")


var = '1+62-3*52'
print(eval(var))
print(256*553-152)
print(2525654//50616 + 2525654%50616)

print("78000원 내기")
a = 78000//50000
b = 78000%50000
print("50000원 짜리 지페는" , a, "장")
c = b//10000
d = b % 10000
print("10000원 짜리 지폐는" , c, "장") 
e = d//5000

print("5000원 짜리 지폐는", e, "장")