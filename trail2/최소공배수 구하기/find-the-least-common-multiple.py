n, m = map(int, input().split())

# Please write your code here.
def LCM(n, m):
    gcd = 0
    for i in range(max(n, m), 0, -1):   # GCD 구하는 부분
        if n % i == 0 and m % i == 0:
            gcd = i
            break

    print(n * m // gcd)                 # LCM 구하는 부분 

LCM(n, m)