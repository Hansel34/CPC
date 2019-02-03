from collections import deque

players, features = map(int, raw_input().split())

q = deque()
visited = set()

def bfs(node):
    for i in range(features):
        new_node = node ^ (1<<i)
        if new_node not in visited:
            q.append(new_node)
            visited.add(new_node)

for _ in range(players):
    player = int(raw_input(),2)
    q.append(player)
    visited.add(player)

while(q):
    current_node = q.popleft()
    bfs(current_node)

print (bin(current_node)[2:].zfill(features))