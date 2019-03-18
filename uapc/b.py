import time
from sys import stdin

points = int(input())
point_set = set()
x_total = 0
y_total = 0

start = time.time()


for _ in range(points):
    x, y = [int(x) for x in input().split()]
    #point_set.add((x,y))
    #x_total+=x
    #y_total+=y


x_mid = x_total/points
y_mid = y_total/points

for point in point_set:
    x,y = point
    x_new = 2*x_mid-x
    y_new = 2*y_mid-y
    if (x_new,y_new) not in point_set:
        print("not symmetric")
        exit()

print("symmetric")

end = time.time()
print(end - start)