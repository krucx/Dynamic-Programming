items = list(map(int,input('Enter the items : ').strip().split()))

def DP(dp,items,parent,i,x,y): ## O(NK^2)
  if x<0 or y<0:
    return 0
  if i>=len(items):
    if x+y==0:
      return 1
    else:
      return 0

  if dp[i][x][y]!=-1:
    return dp[i][x][y]

  list1 = [DP(dp,items,parent,i+1,x-items[i],y),DP(dp,items,parent,i+1,x,y-items[i]),DP(dp,items,parent,i+1,x,y)]
  dp[i][x][y] = max(list1)

  for j in range(3):
    if list1[j]==1 and parent[i]==-1:
      parent[i] = j
      break

  return dp[i][x][y]

def reconstruct_soln(items,parent):
  s = [[],[],[]]
  for i,item in enumerate(items):
    s[parent[i]].append(str(item))
  for i in range(3):
    print('SET {} : {}'.format(i+1,','.join(s[i])))

sum = 0
for i in items:
  sum+=i
if sum%3==0:
  dp = []
  parent = []
  for j in range(len(items)):
    b = []
    for k in range((sum//3)+1):
      c = []
      for l in range((sum//3)+1):
        c.append(-1)
      b.append(c)
    dp.append(b)
    parent.append(-1)
  x = DP(dp,items,parent,0,sum//3,sum//3)
  if x==1:
    print('SOLUTION EXISTS : ')
    reconstruct_soln(items,parent)
  else:
    print('NO SOLUTION')
else:
  print('NO SOLUTION')