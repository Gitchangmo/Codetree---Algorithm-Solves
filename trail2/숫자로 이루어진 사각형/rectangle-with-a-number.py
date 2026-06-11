n = int(input())

# Please write your code here.
def draw_rec(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            print(num, end=' ')
            num += 1
            if num > 9:
                num = 1
        print()

draw_rec(n)