#To divide a number into maximum amount of distinct elements

#Safe move: Starting from 1, increase step by step till where last element is not repeated

def maxDivi(n):
    ele = list()
    sum = 0
    i = 1
    while True:
        if ((n - (sum + i)) <= i):
            ele.append(n - sum)
            break
        ele.append(i)
        sum = sum + i
        i = i + 1
    return ele

#Main function
if __name__ == '__main__':
    n = int(input())
    ele = maxDivi(n)
    print(len(ele))
    print(*ele)