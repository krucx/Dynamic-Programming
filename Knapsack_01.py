weights = list(map(int,input("Enter the weights : ").strip().split()))
value = list(map(int,input("Enter the values : ").strip().split()))
o_capacity = int(input("Enter the capacity : "))

def gcd_of_arr(capacity,weight):
    a = capacity
    for i in weight:
        a = gcd(a,i)
    return a

def gcd(a,b):
    if a*b == 0:
        return a+b
    if a==1 or b==1:
        return 1
    return gcd(b,a%b)

def DP(dp,capacity,i,parent):
  
  if i>= len(weight):
    return 0

  if dp[i][capacity]!= -1:
    return dp[i][capacity]

  elif capacity == 0 or weight[i] > capacity:
    dp[i][capacity] = 0
    return dp[i][capacity]

  else:
    dp[i][capacity] = DP(dp,capacity-weight[i],i+1,parent) + value[i]
    x = DP(dp,capacity,i+1,parent)
    if x>dp[i][capacity]:
      dp[i][capacity] = x
    else:
      parent[dp[i][capacity]] = i
  return dp[i][capacity]

def print_sack(opt_val,parent):  
  ele = []
  val = opt_val 
  while val!=0:
    ele.append(str(weight[parent[val]]*gcd)+":"+str(value[parent[val]]))
    val = val - value[parent[val]]
  return ' ,'.join(ele)

gcd = gcd_of_arr(o_capacity,weights)
weight = [a//gcd for a in weights]
capacity = o_capacity//gcd

dp = []
parent = {}
for i in range(len(weight)):
  row = []
  for j in range(capacity+1):
    row.append(-1)
  dp.append(row)

opt_val = DP(dp,capacity,0,parent)

print("\n\nMAXIMUM VALUE : "+str(opt_val))

print("\n\nWEIGHTS IN KNAPSACK : " + print_sack(opt_val,parent)+"\n")

print("DP TABLE : ")
for i in range(len(weight)):
    s = []
    for j in range(capacity+1):
        if dp[i][j] == -1:
            s.append("U")
        else:
            s.append(str(dp[i][j]))
    print(s)