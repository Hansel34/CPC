test_cases = int(input())
minutes = 0
seconds = 0
for case in range(test_cases):
    m,s = [int(x) for x in input().split()]
    minutes+=m
    seconds+=s
answer = seconds/(minutes*60)
if answer <= 1:
    print("measurement error")
else:
    print(answer)