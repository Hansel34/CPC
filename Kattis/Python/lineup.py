lines = int(input())

names = []

for _ in range(lines):
    names.append(input())

names_i = sorted(names)
names_r = sorted(names,reverse=True)

if names_i == names:
    print("INCREASING")
elif names_r == names:
    print("DECREASING")
else:
    print("NEITHER")