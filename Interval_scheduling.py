#intervals = [(1,3,20),(2,5,20),(3,10,100),(4,6,70),(6,9,60)]

#intervals = sorted(intervals,key = lambda x: x[0])

def take_input():
    intervals = []
    n = int(input("Enter number of intervals : "))
    print("\n\n Input Format start,end,value \n\n")
    for i in range(n):
        x = tuple(map(int,input("Enter the interval "+str(i+1)+": ").strip().split(',')))
        intervals.append(x)
    intervals = sorted(intervals,key = lambda x: x[0])
    return intervals

def after_finish_time(finish_time):
    index = 0
    for x in intervals:
        if x[0]>=finish_time:
            break
        index = index+1
    return index

def print_intervals(parent,max_profit):
  s = []
  f = max_profit
  while parent.get(f,-10)!=-10:
    s.append(str(intervals[parent[f]]))
    f = f - intervals[parent[f]][2]
  return ' '.join(s)        

def DP(dp,parent,i):
    
    if i>=len(intervals):
        return 0

    if dp[i]!=-1:
        return dp[i]

    index = after_finish_time(intervals[i][1])
    x = DP(dp,parent,index) + intervals[i][2]
    y = DP(dp,parent,i+1)
    if x>y:
        dp[i] = x
        parent[dp[i]] = i 
    else:
        dp[i] = y
    return dp[i]

intervals = take_input()

dp = [-1] * len(intervals)
parent = {}
max_profit = DP(dp,parent,0)

print("MAX PROFIT : "+str(max_profit))
print("INTERVALS : "+print_intervals(parent,max_profit))    