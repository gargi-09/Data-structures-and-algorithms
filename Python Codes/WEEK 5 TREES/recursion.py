#find some of n numbers

def sum_n_nums(n):

    if n == 1:
        return 1
    
    return n+sum_n_nums(n-1)

def fib(n):

    if n == 0 or n == 1:
        return n
    return fib(n-1)+fib(n-2)

def sum_int(num):
    if num == 0:
        return num
    return  num%10+sum_int(num//10)

print(sum_int(345))
