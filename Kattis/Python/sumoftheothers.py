while True:
    try:
        numbers = [int(x) for x in input().split()]
        total = sum(numbers)
        for number in numbers:
            if total-number == number:
                print(number)
                break
            
    except EOFError:
        break