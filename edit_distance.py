s1 = input('Enter string 1 : ')
s2 = input('Enter string 2 : ')
INF = 100000

insert_cost = 1
delete_cost = 1
replace_cost = 1

def cost(option):
    if option==1:
        return insert_cost
    elif option==2:
        return delete_cost
    else:
        return replace_cost


def DP(dp,i,j):

    if i>len(s1) and j>len(s2):
        return 0

    if i==len(s1):
        dp[i][j] = len(s2)-j
        return dp[i][j]
    
    if j==len(s2):
        dp[i][j] = len(s1)-i
        return dp[i][j]
    
    if dp[i][j] != INF:
        return dp[i][j]

    if s1[i] == s2[j]:
        dp[i][j] = DP(dp,i+1,j+1)
        return dp[i][j]

    m = min(cost(1)+DP(dp,i,j+1),cost(2)+DP(dp,i+1,j),cost(3)+DP(dp,i+1,j+1))
    dp[i][j] = m
    return dp[i][j]

dp = []
for i in range(len(s1)+1):
    row = []
    for j in range(len(s2)+1):
        row.append(INF)
    dp.append(row)

edit_distance = DP(dp,0,0)

print("\n\nEDIT DISTANCE : "+str(edit_distance)+"\n\n")

print("DP TABLE : ")
for i in range(len(s1)):
    s = []
    for j in range(len(s2)):
        if dp[i][j] == INF:
            s.append("INF")
        else:
            s.append(' '+str(dp[i][j])+' ')
    print(s)
