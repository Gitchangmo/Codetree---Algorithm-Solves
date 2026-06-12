str = input()

# Please write your code here.
stack = []

for s in str:
    if s == '(':
        stack.append(s)
    elif s == ')':
        if not stack:
            print("No")
            exit()
        if stack[-1] == '(':
            stack.pop()

if not stack:
    print("Yes")
else:
    print("No")
