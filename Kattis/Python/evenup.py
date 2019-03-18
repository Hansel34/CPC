total = int(input())

cards = [int(x) for x in input().split()]

stack = []

for n in cards:
    if stack:
        if (n + stack[-1]) % 2 == 0:
            stack.pop()
            continue
        else:
            stack.append(n)
    else:
        stack.append(n)
print(len(stack))