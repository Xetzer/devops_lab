while True:
    try:
        N = int(input("Please enter N from [0;10**9]: "))
        if N < 0 or N > 10 ** 9:
            raise ValueError
        break
    except ValueError:
        print("This input doesn't look like valid N, try again.")

def mults(N):
    Q = -1
    dec = 1
    tmp = 0
    if N <= 9:
        return N
    for i in range(9, 1, -1):
        while N % i == 0:
            tmp += i * dec
            dec *= 10
            N /= i
    if N == 1:
        Q = tmp
    return Q
print(mults(N))

