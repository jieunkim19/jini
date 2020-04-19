# for 구문

#for i in range(1, 6): # * 반복
#    for j in range(6-i): # 공백 반복
#        print(" ", end="")
#    for j in range(i):
#        print("*", end="")
#    print()


# format{:>5}하면 맨 왼쪽에 별출력하고 나머지는 공백으로 출력

for i in range(5):
    print("{:>5}".format("*" * (i +1)))
