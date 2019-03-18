answers = {} 
signs = ['+','-','*','//']
for i in signs:
    for j in signs:
        for k in signs:
            equation = "4{}4{}4{}4".format(i,j,k)
            answer = eval(equation)
            answers[answer] = [i,j,k]
            
test_cases = int(input())

for case in range(test_cases):
    answer = int(input())
    signs = []
    if answer in answers:

        print("4 {} 4 {} 4 {} 4 = {}".format(answers[answer][0],answers[answer][1],answers[answer][2],str(answer)).replace("//","/"))

    else:
        print("no solution")