
while True:

    a = input("다섯자리 정수를 입력하세요")

    sum = 0
    for i in range(len(a)):

        if i == len(a)-1:
            print(a[i], end=' ')
        else:
            print(a[i], end='+')
        sum+=int(a[i])
    print('=',sum)

    response = input("계속하시겠습니까? (y/n)")
    if response == "n" or response == "N":
        print("프로그램 종료")
        break;
