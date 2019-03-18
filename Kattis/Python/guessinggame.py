max_num = 11
min_num = 0
while True:
    number = int(input())
    if number == 0:
        break
    answer = input()
    if answer == "too high":
        max_num = min(number,max_num)
    elif answer == "too low":
        min_num = max(number,min_num)
    else:
        if number > min_num and number < max_num:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        max_num = 11
        min_num = 0