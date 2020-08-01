# To calculate Fn modulo m

#Pisano's Period: For any integer 𝑚 ≥ 2, the sequence 𝐹𝑛 mod 𝑚 is periodic.
#The period always starts with 0 1 and period cannot be found using a mathematical equation

#Naive Code
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

#Fast code

#To check if the list is periodic
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
def get_fibonacci_huge_fast(n, m):
    fib = get_period(m)
    l = len(fib)
    return fib[n%l]
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    #print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))