arr = [input() for _ in range(10)]
word = input()
F_flag = 1
for s in arr:
    if s[-1] == word:
        print(s)
        F_flag = 0

if F_flag:
    print('None')