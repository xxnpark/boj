M, N = map(int, input().split())

def is_prime(n):
    if n == 1:
        return False
    for m in range(2, int(n**(1/2))+1):
        if n % m == 0:
            return False
    return True

for n in range(M, N+1):
    if is_prime(n):
        print(n)