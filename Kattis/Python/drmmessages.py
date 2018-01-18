drmMessage = input()

lengthDrm = len(drmMessage)
firstHalf = drmMessage[:lengthDrm//2]
secondHalf = drmMessage[lengthDrm//2:]


A = ord('A')
totalSumFirst = 0
totalSumSecond = 0


for char in firstHalf:
	totalSumFirst+= ord(char)-A

for char in secondHalf:
	totalSumSecond+= ord(char)-A

answerFirst = ""
answerSecond = ""

for char in firstHalf:
	answer = totalSumFirst+ord(char)-A
	while answer > 25:
		answer -= 26
	answer += A
	answerFirst += chr(answer)

for char in secondHalf:
	answer = totalSumSecond+ord(char)-A
	while answer > 25:
		answer -= 26
	answer += A
	answerSecond += chr(answer)
	
finalAnswer = ""
for x in range(len(answerFirst)):
	answer = ord(answerFirst[x])+ord(answerSecond[x])-A-A
	while answer > 25:
		answer -= 26
	answer += A
	finalAnswer += chr(answer)


print(finalAnswer)
