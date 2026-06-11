A = input()

sum = 0

for w in A:
    if w.isdigit():
        sum += ord(w) - ord('0')

print(sum)