# To find the last digit of sum of Fibonacci numbers from Fm to Fn

#Trick is sum of first n Fibonacci numbers is (F(n+2)-1)
#Therefore to find the last digit it is (F(n+2)-1) modulo 10
#The period of Fn modulo 10 can be found in the previous program and must be used here

#All we do here is to subtract the last digit of the summation Fm-1 from Fn

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
def fibonacci_partial_sum_fast(m, n):
    fib = get_period(10)
    l = len(fib)
    num1 = fib[(n+2)%l] - 1 #Last digit of Fn
    if num1 == -1: num1 = 9
    num2 = fib[(m+1)%l] - 1 #Last digit of Fm
    if num2 == -1: num2 = 9
    num1 = num1 + 10
    return (num1 - num2) % 10   

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum_fast(m, n))