import math
a,b = [int(x) for x in input().split('/')]
numerator = (a-32*b)*5
denominator = (b*9)

greatest = int(math.gcd(numerator,denominator))

print(str(int(numerator/greatest))+ "/" + str(int(denominator/greatest)))

