A = input()
B = input()

# Please write your code here.
while B in A:
    sub = A.find(B)
    A = A[:sub] + A[sub+len(B):]

print(A)