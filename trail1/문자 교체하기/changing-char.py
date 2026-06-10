str1, str2 = input().split()

arr1 = list(str1)
arr2 = list(str2)

temp = arr1[:2]
arr2 = temp + arr2[2:]

print(''.join(arr2))