from collections import defaultdict

while True:

    files = int(input())

    if files == 0:
        break

    unique_files = defaultdict(int)
    hash_amounts = defaultdict(int)
    hash_collisions = 0
    for _ in range(files):

        line = input()

        hash = ord(line[0])

        if len(line) > 1:
            for c in line[1:]:
                hash = hash ^ ord(c)

        hash_amounts[hash] += 1
        unique_files[line]+=1

        hash_collisions += hash_amounts[hash]-unique_files[line]

    
    print(len(unique_files),hash_collisions)