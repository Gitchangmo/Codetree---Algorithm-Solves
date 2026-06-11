A = input()
B = input()

N = -1
for i in range(len(A)):
    A = A[-1] + A[:-1]
    if A == B:
        N = i+1
        break

print(N)