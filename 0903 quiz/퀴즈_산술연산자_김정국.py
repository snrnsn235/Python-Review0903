'''
num1, num2, num3, num4, num5, sum=0,0,0,0,0,0

num1=int(input("다섯자리 정수를 입력하시오!! "))
num2=int(input("다섯자리 정수를 입력하시오!! "))
num3=int(input("다섯자리 정수를 입력하시오!! "))
num4=int(input("다섯자리 정수를 입력하시오!! "))
num5=int(input("다섯자리 정수를 입력하시오!! "))

sum=num1+num2+num3+num4+num5
print("%d + %d + %d + %d + %d = %d" % (num1,num2,num3,num4,num5, sum))
print("계속하려면 아무 키나 누르십시오...")
'''

aa=[ ]
sum = 0

for i in range(0,5,1) :
    aa.append(0)
    aa[i] = int(input( str(i+1) + "번째 숫자 : "))
    sum += aa[i]
print(" =%d " % sum)

