
test_cases = int(input())

for _ in range(test_cases):
    grades = [int(x) for x in input().split()]
    avg = sum(grades[1:])/grades[0]

    count = 0
    for grade in grades:
        if grade > avg:
            count+=1
    
    print("{0:.3f}%".format(round(count/grades[0]*100,3)))
