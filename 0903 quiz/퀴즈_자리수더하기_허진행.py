while 1:
    n = int(input("다섯자리 정수를 입력하시오!!\n"))
    a = n//10000
    b = (n%10000)//1000
    c = (n%1000)//100
    d = (n%100)//10
    e = n%10
    dap = a + b + c + d + e

    print(a, "+", b, "+", c, "+", d, "+", e, "=", dap)
    con=""
    con=input("그만두려면 no를\n계속하려면 아무키나 누르십시오\n")
    if con =="no":
        break
    else :
        continue

    

