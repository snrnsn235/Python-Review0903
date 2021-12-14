# 5자리 입력 받아, 각 자릿수 모두 더하기

while True :
    tSum =0
    inNum =int(input("5자리값 입력 : "))
    nam =inNum
    
    for i in range(5,0,-1):
    
        mok = nam //(10**(i-1))
        nam = nam %(10**(i-1))
        tSum = tSum + mok

    print(tSum)
    print('')
 

