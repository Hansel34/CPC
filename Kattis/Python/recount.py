from collections import Counter
peoples = []
while True:
    person = input()
    if person == "***":
        break
    peoples.append(person)

peoples = Counter(peoples)
most_common = peoples.most_common(2)

if most_common[0][1] == most_common[1][1]:
    print("Runoff!")
else:
    print(most_common[0][0])