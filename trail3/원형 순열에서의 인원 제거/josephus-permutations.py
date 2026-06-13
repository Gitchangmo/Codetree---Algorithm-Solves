from collections import deque

n, k = map(int, input().split())

Q = deque()

for i in range(1, n+1):
    Q.append(i)

while Q:
    for _ in range(1, k):
        Q.append(Q.popleft())
    print(Q.popleft(), end=' ')