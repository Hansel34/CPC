from collections import deque

while True:
    try:
        pattern = raw_input()
        text = raw_input()

        pattern_d = 0
        prime_number = 97
        mod = 10**9 + 9
        text_d = 0
        
        answer = []
        for i,c in enumerate(pattern):
            pattern_d += ord(c) * (prime_number**i)
        pattern_d = pattern_d % mod

        for i,c in enumerate(text):
            if i < len(pattern):
                text_d += ord(c) * (prime_number**i)
                if i == len(pattern)-1:
                    text_d = text_d % mod
            else:
                if pattern_d == text_d:
                    answer.append(i-len(pattern))
                text_d -= ord(text[i-len(pattern)])
                text_d /= prime_number
                text_d += ord(c) * (prime_number**(len(pattern)-1)% mod)
                
        if pattern_d == text_d:
            answer.append(len(text)-len(pattern))

        print(" ".join([str(x) for x in answer]))
    except EOFError:
        break