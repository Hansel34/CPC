test_case = int(input())

for _ in range(test_case):
    sounds = [sound for sound in input().split()]
    while True:
        line = input()
        if line == "what does the fox say?":
            print(" ".join(sounds))
            break
        else:
            line = line.split()
            while line[2] in sounds:
                sounds.remove(line[2])