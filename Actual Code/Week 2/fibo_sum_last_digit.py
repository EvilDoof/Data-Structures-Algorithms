# To find the last digit of sum of first n Fibonacci numbers

#Trick is sum of first n Fibonacci numbers is (F(n+2)-1)
#Therefore to find the last digit it is (F(n+2)-1) modulo 10
#The period of Fn modulo 10 can be found in the previous program and must be used here

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

#Fast Code
def check_list_period(lst):
    mid = len(lst) // 2
    if (lst[:mid] == lst[mid:]):
        return mid
    else:
        return 0

#To check obtain the fibonacci remainder list
def get_period(m):
    fib = [0, 1]
    while True:
        fib.append((fib[-1] + fib[-2]) % m)
        period = check_list_period(fib)
        if period != 0:
            return fib[:period]

#To calculate Fn modulo m
def fibonacci_sum_fast(n):
    fib = get_period(10)
    l = len(fib)
    num = fib[(n+2)%l]
    if num == 0:
        return 9
    else:
        return num - 1

if __name__ == '__main__':
    n = int(input())
    #print(fibonacci_sum_naive(n))
    print(fibonacci_sum_fast(n))