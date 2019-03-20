test_case = int(input())
st = "welcome to code jam"
for i in range(test_case):
    string = [c for c in st]
    dp = [0]*(len(string)+1)
    for c in input():
        if c == 'w':
            dp[1]+=1
        for index,cc in enumerate(string):
            if cc==c:
                dp[index+1]+=dp[index]
    dp[len(string)] = dp[len(string)] % 10000
    print("Case #{}: {}".format(i+1,str(dp[len(string)]).zfill(4)))