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

def DP(dp,parent,finish_time):

    index = after_finish_time(finish_time)

    if index>=len(intervals):
        return 0

    if dp[index]!=-1:
        return dp[index]

    dp[index] = 0
    j = index
    for i in range(index,len(intervals)):
        x = DP(dp,parent,intervals[i][1]) + intervals[i][2]
        if x>dp[index]:
            dp[index] = x
            j = i
    
    parent[dp[index]] = j
    return dp[index]

intervals = take_input()

dp = [-1] * len(intervals)
parent = {}
max_profit = DP(dp,parent,0)

print("MAX PROFIT : "+str(max_profit))
print("INTERVALS : "+print_intervals(parent,max_profit))    