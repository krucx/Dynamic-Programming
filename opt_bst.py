ele = list(map(int,input("\nEnter the elements (in sorted order) : ").strip().split()))
freq = list(map(int,input("\nEnter the frequencies : ").strip().split()))
INF = 1000000

def DP(dp,child,i,j,level):
    
    if i<0 or j>=len(ele) or i>=len(ele) or j<0 or i>j:
        return 0

    if dp[i][j][level-1] != -1:
        return dp[i][j][level-1]

    if i==j:
      return freq[i]*level

    root = -1
    minimum = INF
    for k in range(i,j+1):
        x = DP(dp,child,i,k-1,level+1) + DP(dp,child,k+1,j,level+1) + freq[k]*level
        if x < minimum:
            minimum = x
            root = k

    dp[i][j][level-1] = minimum
    child[i][j] = root

    return dp[i][j][level-1] 

def inorder(child,i,j):
   
    if i<0 or j>=len(ele) or i>=len(ele) or j<0 or i>j:
        return 0
    k = child[i][j]

    if i==j:
      print(ele[i])

    if k==-1:
      return 0

    inorder(child,i,k-1)
    print(ele[k])
    inorder(child,k+1,j)

def postorder(child,i,j):
  
    if i<0 or j>=len(ele) or i>=len(ele) or j<0 or i>j:
        return 0
    k = child[i][j]

    if i==j:
      print(ele[i])

    if k==-1:
      return 0

    postorder(child,i,k-1)
    postorder(child,k+1,j)
    print(ele[k])

dp = []
child = []
for i in range(len(ele)):
    row = []
    r = []
    for j in range(len(ele)):
      c = []
      for k in range(len(ele)):
        c.append(-1)
      r.append(c)
      row.append(-1)
    dp.append(r)
    child.append(row)

cost = DP(dp,child,0,len(ele)-1,1)

print("MINIMUM SEARCH COST : " + str(cost))

print("INORDER :")
inorder(child,0,len(ele)-1)
print("POSTORDER :")
postorder(child,0,len(ele)-1)
    