answer = set(input())
alphabet = input()
wrongs = 0

for c in alphabet:
    if c in answer:
        answer.remove(c)
    else:
        wrongs+=1
    if wrongs == 10:
        print("LOSE")
        exit()
    if not answer:
        break


print("WIN")

