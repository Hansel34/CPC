# Read the following for more information. 
# Proof and code for formula shown below, would just memorize.
# https://www.geeksforgeeks.org/last-non-zero-digit-factorial/

dig= [1, 1, 2, 6, 4, 2, 2, 4, 2, 8] 
   
def lastNon0Digit(n): 
    if (n < 10): 
        return dig[n] 
   
    if (((n//10)%10)%2 == 0): 
        return (6*lastNon0Digit(n//5)*dig[n%10]) % 10
    else: 
        return (4*lastNon0Digit(n//5)*dig[n%10]) % 10
    return 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(lastNon0Digit(n))
