def prime(n):
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True

def unicos(L):
    out_L = []
    for i in L:
        if i not in out_L:
            out_L.append(i)
    return out_L

def amigavel(ab):
    sum_a = 0
    for i in range(1, ab[0]):
        if ab[0] % i == 0:
            sum_a += i
    sum_b = 0
    for i in range(1, ab[1]):
        if ab[1] % i == 0:
            sum_b += i
    return sum_a == ab[1] and sum_b == ab[0]

def sort(L):
    return (sort([y for y in L[1:] if y <  L[0]]) +
            L[:1] +
            sort([y for y in L[1:] if y >= L[0]])) if len(L) > 1 else L
