S, Q = input().split()
Q = int(Q)

arr = list(S)

for i in range(Q):
    Query = list(input().split())
    if int(Query[0]) == 1:
        a = int(Query[1])
        b = int(Query[2])
        temp = arr[a-1]
        arr[a-1] = arr[b-1]
        arr[b-1] = temp
        print(''.join(arr))
    elif int(Query[0]) == 2:
        for idx, w in enumerate(arr):
            if w == Query[1]:
                arr[idx] = Query[2]
        print(''.join(arr))