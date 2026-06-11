n, m = map(int, input().split())

# Please write your code here.
def draw_rectangle(n, m):
    for _ in range(n):
        print('1' * m)

draw_rectangle(n, m)