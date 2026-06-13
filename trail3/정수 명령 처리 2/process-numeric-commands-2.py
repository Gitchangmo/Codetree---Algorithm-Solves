from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def pop(self):
        return self.dq.popleft()

    def size(self):
        return len(self.dq)

    def empty(self):
        return not self.dq

    def front(self):
        return self.dq[0]


N = int(input())
Q = Queue()

for _ in range(N):
    line = input().split()

    if line[0] == "push":
        A = int(line[1])
        Q.push(A)
    elif line[0] == 'pop':
        print(Q.pop())
    elif line[0] == 'size':
        print(Q.size())
    elif line[0] == 'empty':
        print(int(Q.empty()))
    elif line[0] == 'front':
        print(Q.front())

# Please write your code here.

