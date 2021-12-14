hap = 0
num = int(input("다섯자리 정수를 입력하시오!\n"))
if(num >= 10000 & num < 100000) :
    num = list(str(num))
    for i in range(0,5) :
        hap += int(num[i])
    print("{} + {} + {} + {} + {} = {}".format(num[0], num[1], num[2], num[3], num[4], hap))

    
