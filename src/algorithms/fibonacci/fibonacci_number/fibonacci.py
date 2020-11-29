# Uses python3

def calc_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = []
    result.append(0)
    result.append(1)
    for i in range(2, n+1):
        result.append(result[i-1] + result[i-2])
    return result[n]
    

def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
