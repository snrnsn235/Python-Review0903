# 변수 선언
sum, tmp, number = 0, 0, 0;

# 정수 입력
while number > 99999 or number < 10000 :
    number = int(input("다섯자리 정수를 입력하시오!!\n"))
    
# 정수 분활하여 더하기
for i in range(4, -1, -1) : 
    tmp = number // (10 ** i)
    number = number % (10 ** i)
    sum += tmp
    print(tmp, end=" ")
    if i > 0 :
        print("+", end=" ")
print("=", sum)
