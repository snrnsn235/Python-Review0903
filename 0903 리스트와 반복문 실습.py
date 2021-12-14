#리스트와 반복문 실습
#for i in range
'''
for i in range(1, 10, 2):
    print(i)
print()
#for 변수 in 리스트
for i in [1,3,5,7,9]:
    print(i)
print()
#for 변수 in 리스트
for i in ["국어", "수학", "국사", "영어", "과학"]:
    print(i)
print()
'''
'''
list1 = ["국어", "수학", "국사", "영어", "과학"]
list2 = ["국어", "수학", "국사", 100, 200]
list3 = ["국어", "수학", "국사", 100, [1,2,3]]
for i in list3:
    print(i)
print()
'''
'''
a='빅테이터'
print(a[0], end="") #빅테이터를 문자열 리스트로 보는것 
print(a[1], end="")
print(a[2], end="")
print(a[3], end="")
print()
for i in range(len(a)):
    print(a[i], end="")
'''
'''
print()

b='48612'
print(b[0]+b[1]+b[2]+b[3]+b[4])
print(int(b[0])+int(b[1])+int(b[2])+int(b[3])+int(b[4]))

sum=0
for i in range(len(b)):
    print(b[i], end="")
    sum+=int(b[i])
print("")
print(sum)
'''
'''
#quiz
#순차탐색: 최소값 최대값 처럼 특정값 찾기 프로그램에서 많이 사용함
#리스트와 반복문 활용
#num=[8,7,3,2,9,4,1,6,5]
#이력 받은 숫자 중 특정 값 찾기

num=[8,7,3,2,9,4,1,6,5]
max, min = 0, 10
for i in num:
    if max < i:
        max = i
    if min > i:
        min = i
print("최대값 : ", max)
print("최소값 : ", min)
'''
'''
##함수 정의 부분
def plus(v1,v2):
    result=0;
    result=v1+v2
    return result
##변수 선언 부분
hap=0

##메인 코드 부분
'''
'''
hap=plus(100,200)
print("100과 200의 plus() 함수 결과는 %d" %hap)
'''
'''
##메인 코드 부분_응용(입력받기)
input1=int(input("더할 숫자를 입력하세요 :"))
input2=int(input("더할 숫자를 입력하세요 :"))
hap = plus(input1,input2)
print("%d와 %d의 plus()함수 결과는 %d" %(input1, input2, hap))
'''
'''
##함수 정의 부분
def calc(v1, v2, op):
    result=0
    if op == '+':
        result=v1+v2
    elif op == '-':
        result=v1-v2
    elif op == '*':
        result=v1*v2
    elif op == '/':
        result=v1/v2

    ##return result
        return result,v1,v2
    
##변수 선언 부분
res=0
va1, va2, oper = 0,0,""

##메인 코드 부분
oper = input("계산 입력(+,-,*,/):")
var1 = int(input("첫번째 숫자 입력 : "))
var2 = int(input("두번째 숫자 입력 : "))

res=calc(var1, var2, oper)
res,v1,v2 = calc(var1, var2, oper)
#print("##계산기 : %d %s %d = %d" %(var1, oper, var2, res))
print("##계산기 : %d %s %d = %d" %(v1, oper, v2, res))
'''
'''
##함수 정의 구분
def para_func(*para): #para는 매개변수(숫자를 정해놓지 않음)
    result=0
    for num in para :
        result=result + num
    return result
##변수 선언 부분
hap=0
##메인 코드 부분
hap=para_func(10,20)
print("매개변수 2개 함수 호출 결과 ==> %d" %hap)
hap=para_func(10,20,30,40,50)
print("매개변수 3개 함수 호출 결과 ==> %d" %hap)
'''
'''
import random

##함수 정의 부분
def getNumber() :
    return random.randrange(1,46) ##rnadrange는 앞에 넣은 값 이상 뒤에 넣은 값 미만의 임의의 정수값 생성 
##변수 선언 부분
lotto = [] #빈 리스트 생성
num=0
##메인(main)코드 부분
print("**로또 추첨을 시작합니다** \n");

while True:
    num=getNumber()

    if lotto.count(num)==0: #추출한 숫자가 이미 뽑힌 숫자와 동일한 숫자가 없다면 리스트에 숫자 추가
        lotto.append(num)
    if len(lotto)>=6: # 리스트의 개수가 6이 될 경우 빠져나옴
        break
print("추첨된 로또 번호==> ", end='')
lotto.sort()#리스트 항목 정렬
for i in range(0, 6):
    print("%d "%lotto[i],end='')
'''
'''
import sys
print(sys.builtin_module_names)
'''
def plus(num1, num2):
    return num1+num2
def minus(num1, num2):
    return num1-num2
def multiply(num1, num2):
    return num1*num2
def divide(num1, num2):
    if num2 != 0:
        return num1/num2
    else :
        print("0으로 나누면 안되요")
        return-1









































