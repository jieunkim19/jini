# 크리스마스 트리~~

#for i in range(1, 10): # 별 출력
#    for j in range(10-i): # 공백 출력
#        print(" ", end="")
#    for j in range(2*i -1):
#        print("*", end="")
#    print()


# format{:^5}하면 별 가운데에 출력, 나머지 공백

for i in range(1, 9, 2):
    print("{:^9}".format("*" * i))
