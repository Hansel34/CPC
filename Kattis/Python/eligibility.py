test_cases = int(input())
uni_start = 2010
birth_start = 1991

for test in range(test_cases):
    name, start_date, birth_date, courses = input().split()

    start_date = start_date.split("/")
    birth_date = birth_date.split("/")

    if int(start_date[0]) >= uni_start:
        print("{} {}".format(name,"eligible"))
        continue
    if int(birth_date[0]) >= birth_start:
        print("{} {}".format(name,"eligible"))
        continue
    if int(courses) <=40:
        print("{} {}".format(name,"coach petitions"))
        continue
    print("{} {}".format(name,"ineligible"))