#To find the last digit sum of squares of first n Fibunacci numbers

#Trick here is that the squares of the fibonacci numbers for a rectangle, with each consecutive square having edge length
#Fn = Fn-1 + Fn-2 thus forming the golden ratio spiral
#Thus always a rectangle is formed of dimensions Fn * Fn + Fn-1
#To calculate the last digit, we use the Pisano's period of 10

#Fast code

#To check if the list is periodic
def check_list_period(lst):
    mid = int(len(lst) / 2)
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
def fibo_sq_sum(n):
    fib = get_period(10)
    period = len(fib)
    l = fib[n%period]
    b = fib[(n-1)%period]
    return (l * (l + b)) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibo_sq_sum(n))

