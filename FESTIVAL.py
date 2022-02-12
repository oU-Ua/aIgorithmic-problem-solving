test_case = int(input())

for i in range(0,test_case):
    n = input()
    l = input()
    num_list = list(map(int, input().split()))
    min_cost(num_list, n, l)


def min_cost(list, b, a):
    sum = 1000
    for i in range (a,b):
        for j in range (0,b-i):
            for k in range (j,j+i):
                a=list[k]
        i=i+1

