# Uses python3


def max_pairwise_product(n):
    result = 0
    
    if len(n) == 0:
        result = 0
    elif len(n) == 1:
        result = n[0]
    elif len(n) == 2:
        result = n[0]*n[1]
    else:
        index_1 = 1
        for i in range(0, len(n)):
            if n[i] > n[index_1]:
                index_1 = i

        if index_1 == 1:
            index_2 = 2
        else:
            index_2 = 1
        for i in range(0, len(n)):
            if i != index_1 and n[i] > n[index_2]:
                index_2 = i
        result = n[index_1] * n[index_2]
    print(result)

    return result


def max_pairwise_product_naive(n):
    result = 0
    for i in range(0, len(n)):
        for j in range(i+1, len(n)):
            if n[i]*n[j] > result:
                result = n[i]*n[j]

    print(result)
    return result


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)

    max_pairwise_product(a)
