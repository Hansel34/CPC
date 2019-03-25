from collections import defaultdict

files = int(input())

dependecies = defaultdict(list)
visited = set()
for _ in range(files):
    d = input().split()

    if len(d) > 1:
        for f in d[1:]:
            dependecies[f].append(d[0][:-1])

# dfs
start = input()
output = []
stack = [start]

while stack:
    no_d = True
    for f in dependecies[stack[-1]]:
        if f not in visited:
            stack.append(f)
            no_d = False
    if no_d:
        pop_file = stack.pop()
        output.append(pop_file)
        visited.add(pop_file)
for f in output[::-1]:
    print(f)

