S = input()

for w in S:
    if w.isdigit():
        print(w, end='')
    elif w.isalpha():
        print(w.lower(), end='')
    else:
        continue