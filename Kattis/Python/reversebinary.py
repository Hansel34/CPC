binaryValue = bin(int(input()))
binaryValue = binaryValue[::-1]
binaryValue = binaryValue[:-2]
intValue = int(binaryValue,2)

print(intValue)


