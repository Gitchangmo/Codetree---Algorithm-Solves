A = input()
Q = input()

for w in Q:
    if w == 'L':
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]

print(A)