N1, N2 = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

is_True = False
for i in range((len(A) - len(B)) + 1):
    temp_A = A[i:i+len(B)]
    is_True = True
    for j in range(len(B)):
        if temp_A[j] != B[j]:
            is_True = False
            break
    if is_True:
        break

if is_True:
    print("Yes")
else:
    print("No")