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
#import Func
#from 모듈명 import 함수1 함수2 함수3
from Func import func1, func2, func3
#from Func import*

##메인 코드 부분

Func.func1()
Func.func2()
Func.func3()

func1()
func2()
func3()
'''

import sys
print(sys.builtin_module_names)
