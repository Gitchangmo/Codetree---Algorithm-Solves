S = input()

result = ''
for w in S:
    if (w >= 'a' and w <= 'z') or (w >= 'A' and w <= 'Z'):
        result += w

print(result.upper())