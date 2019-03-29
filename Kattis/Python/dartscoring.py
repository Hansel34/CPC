from math import hypot
# Implementation of convex hull copied from
# https://leetcode.com/problems/erect-the-fence/discuss/103300/Detailed-explanation-of-Graham-scan-in-14-lines-(Python)
def cross(p1, p2, p3):
    return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)


def slope(p1, p2):
    return 1.0*(p1.y-p2.y)/(p1.x-p2.x) if p1.x != p2.x else float('inf')

def calculate_distance(p1,p2):
    return hypot(p1.x-p2.x,p1.y-p2.y)

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

while True: 
    try:
        coords = [float(x) for x in input().split()]
        points = []
        for i in range(0,len(coords),2):
            points.append(point(coords[i],coords[i+1]))
        n = len(points)
        start = min(points, key=lambda p: (p.x, p.y))
        points.pop(points.index(start))

        points.sort(key=lambda p: (slope(p, start), -p.y, p.x))
 
        ans = [start]
        for p in points:
            ans.append(p)
            while len(ans) > 2 and cross(ans[-3], ans[-2], ans[-1]) < 0:
                ans.pop(-2)
        ans.append(ans[0])
        total_d = 0
        for i in range(len(ans)-1):
            total_d+=calculate_distance(ans[i],ans[i+1])
        print (100*n/(1+total_d))
    except EOFError:
        break