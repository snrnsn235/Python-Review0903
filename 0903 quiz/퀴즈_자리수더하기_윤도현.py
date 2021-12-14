a, b, c, d, e, result, num = 0, 0, 0, 0, 0, 0, 0
while(True):
    
    num = int(input("다섯자리 숫자를 입력하시오! :"))
                     
    a=num // 10000
    num %= 10000

    b=num // 1000
    num %= 1000

    c = num // 100
    num %= 100

    d = num // 10
    num %= 10

    e = num

    result = a + b + c + d +e
                     
    print(a, "+", b ,"+", c, "+", d, "+", e, "=", result)
