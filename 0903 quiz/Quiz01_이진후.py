while (True):
    print("다섯자리 정수를 입력하시오!!")
    num=int(input())

    if int(num/10000) == 0 or int(num/10000) >= 10:
        continue

    num1 = int(num / 10000)
    num = num - num1 * 10000

    num2 = int(num / 1000)
    num = num - num2*1000

    num3 = int(num / 100)
    num = num - num3*100

    num4 = int(num / 10)
    num = num - num4*10

    hap = num1 + num2 + num3 + num4 + num
    print("%d + %d + %d + %d + %d = %d" %(num1, num2, num3, num4, num, hap))

    print("계속하려면 아무 키나 누르십시오...")
    n=input()
