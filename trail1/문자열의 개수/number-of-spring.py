count = 0

result = []
while True:
    S = input()
    if S == '0':
        break
    count += 1
    if count % 2 == 1:
        result.append(S)

print(count)

for w in result:
    print(w)