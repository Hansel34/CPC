# N number of players
# K number of legs
# Players are across top of page
# Characters are at the bottom
from sys import stdin
#connect lines

chars, legs = [int(x) for x in stdin.readline().split()]
all_legs = []

for _ in range(legs):
    index, height = [int(x) for x in stdin.readline().split()]
    all_legs.append([height,index])

all_legs.sort()

chararacters = [x for x in range(chars)]

for leg in all_legs:
    index = leg[1]
    chararacters[index], chararacters[index+1] = chararacters[index+1], chararacters[index]
answer = [0]*chars

for index,char in enumerate(chararacters):
    answer[char] = index

print(" ".join([str(x) for  x in answer]))
