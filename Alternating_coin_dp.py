coins = list(map(int,input('Enter the coins : ').strip().split()))

INF = 10000000

def DP(dp,i,j,sign,parent):

  if i>j or i>=len(coins) or j<0:
    return 0

  if i==j:
    dp[i][j] = sign*coins[i]
    parent[dp[i][j]] = i
    return dp[i][j]
  
  if dp[i][j]!=INF:
    return dp[i][j] 

  max = DP(dp,i+1,j,-sign,parent) + sign*coins[i]
  choice = i
  y = DP(dp,i,j-1,-sign,parent) + sign*coins[j]
  if (y>max and sign==1) or (y<max and sign==-1):
    max = y
    choice = j

  dp[i][j] = max
  parent[dp[i][j]] = choice

  return dp[i][j]  

def regenerate_moves(parent,value):
  v = value
  s = []
  for i in range(len(coins)):
    if i%2==0:
      s.append('First player takes : '+str(coins[parent[v]])+'\n')
      v = v - coins[parent[v]]
    else:
      s.append('Second player takes : '+str(coins[parent[v]])+'\n')
      v = v + coins[parent[v]]
  return ''.join(s)

dp = []
parent = {}
for i in range(len(coins)):
  row = []
  for j in range(len(coins)):
    row.append(INF)
  dp.append(row)

value = DP(dp,0,len(coins)-1,1,parent)

print('MOVES : \n')
print(regenerate_moves(parent,value))
print('Total value of first player ' + str((sum(coins)-value)//2+value))