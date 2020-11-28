coins = list(map(int,input('Enter the coins : ').strip().split()))

INF = 10000000

def maximum(x,y):
  if x>=y:
    return x,1
  return y,2

def DP1(dp,i,j,parent):

  if i>j or i>=len(coins) or j<0:
    return 0

  if i==j:
    dp[i][j] = coins[i]
    parent[dp[i][j]] = i
    return dp[i][j]

  if dp[i][j]!=INF:
    return dp[i][j]

  dp[i][j],pos = maximum(min(DP1(dp,i+1,j-1,parent),DP1(dp,i+2,j,parent))+coins[i],min(DP1(dp,i,j-2,parent),DP1(dp,i+1,j-1,parent))+coins[j])
  
  parent[dp[i][j]] = i
  if pos==2:
    parent[dp[i][j]] = j
  
  return dp[i][j]

def first_player_moves(parent,opt):
  o = opt
  s = []
  while o>0:
    s.append('First player takes : '+str(coins[parent[o]])+'\n')
    o = o - coins[parent[o]]
  return ''.join(s)

dp = []
parent = {}
for i in range(len(coins)):
  row = []
  for j in range(len(coins)):
    row.append(INF)
  dp.append(row)

opt = DP1(dp,0,len(coins)-1,parent)

print('FIRST PLAYER MOVES : \n')
print(first_player_moves(parent,opt))
print('Total value of first player ' + str(opt))