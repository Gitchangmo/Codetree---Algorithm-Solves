N = int(input())

count = 0

result = [N * i for i in range(1, 11)]

for num in result:
    print(num, end=' ')
    if num % 5 == 0:
        count += 1
        if count > 1:
            break
