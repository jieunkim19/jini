#변수 선언
counter=0

def fibonacci(n):

    print("fibonacci({})를 구한다.".format(n))
    global counter
    counter +=1

    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)
print("----")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번이다.".format(counter))


