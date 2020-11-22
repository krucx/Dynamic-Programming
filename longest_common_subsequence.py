s1 = input("Enter first String : ")
s2 = input("Enter second String : ")

def DP(dp,i,j):

    if i>=len(s1) or j>=len(s2):
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i]==s2[j]:
        dp[i][j] = 1 + DP(dp,i+1,j+1)
        return dp[i][j]
    
    dp[i][j] = max(DP(dp,i+1,j),DP(dp,i,j+1))
    return dp[i][j]

dp = []
for i in s1:
    row = []
    for j in s2:
        row.append(-1)
    dp.append(row)

length = DP(dp,0,0)

print('\n LENGTH OF LONGEST COMMON SUBSEQUENCE : '+str(length)+"\n")

print("DP TABLE : ")
for i in range(len(s1)):
    s = []
    for j in range(len(s2)):
        if dp[i][j] == -1:
            s.append("-1 ")
        else:
            s.append(' '+str(dp[i][j])+' ')
    print(s)