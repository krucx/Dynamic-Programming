first_dims = list(map(int,input("\nEnter the numbers : ").strip().split()))
INF = 1000000

def todims(first_dims):
    dims = []
    for i in range(len(first_dims)-1):
        dims.append([first_dims[i],first_dims[i+1]])
    return dims

def cost(i,k,j):
    return i*k*j

def DP(dp,split,i,j):
  
  if i>=j:
    return 0    

  elif dp[i][j]!=INF:
    return dp[i][j]

  else:
    min = DP(dp,split,i,i) + DP(dp,split,i+1,j) + cost(dims[i][0],dims[i][1],dims[j][1])
    opt = i
    for k in range(i+1,j):
        x = DP(dp,split,i,k) + DP(dp,split,k+1,j) + cost(dims[i][0],dims[k][1],dims[j][1])
        if x < min:
          min = x
          opt = k
    dp[i][j] = min
    split[i][j] = opt
    return dp[i][j]

def paranthesis(before,after,split,i,j):
  
  if i>=j:
    return
  
  before[i] += 1
  after[j] += 1
  k = split[i][j]
  paranthesis(before,after,split,i,k)
  paranthesis(before,after,split,k+1,j)

def print_paranthesis(before,after):
  s = []
  for i in range(len(dims)):
    s.append(("("*before[i])+chr(i+65)+(")"*after[i]))
  return ''.join(s)

dims = todims(first_dims)

dp = []
split = []
for i in range(len(dims)):
    row = []
    p = []
    for j in range(len(dims)):
        p.append(-1)
        if i==j:
            row.append(0)
        else:
            row.append(INF)
    dp.append(row)
    split.append(p)

DP(dp,split,0,len(dims)-1)

before = [0]*len(dims)
after = [0]*len(dims)
paranthesis(before,after,split,0,len(dims)-1)

print("\n\n OPTIMAL PARANTHESIZATION IS : " + print_paranthesis(before,after))