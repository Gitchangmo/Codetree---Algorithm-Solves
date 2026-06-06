N = int(input())
arr = [input() for _ in range(N)]
word = input()

temp = ''
count = 0

for s in arr:
    if s[0] == word:
        count += 1
        temp += s

Avg = len(temp) / count
print(f"{count} {Avg:.2f}")