print("\n Enter the text you want to justify")
text = input()
words = text.split()
print("\n Enter the maximum width of line")
total_width = int(input())
INF = 10000000

def badness(i,j):
    line_width = 0
    for r in range(i,j):
        line_width = line_width + len(words[r]) + 1
    line_width = line_width - 1
    if(line_width>total_width):
        return INF
    return (total_width-line_width)**3

def DP(i,dp,next):
    if(dp[i]!=INF):
        return dp[i]
    min = INF
    j = i+1
    for r in range(i+1,len(words)+1):
        x = DP(r,dp,next)+badness(i,r)
        if(x<min):
            min = x
            j = r
    dp[i] = min
    next[i] = j
    return dp[i]

def justified_text(words,next):
  prev = 0
  while next.get(prev,-1)!=-1:
    i = next[prev]
    print(' '.join(words[prev:i]))
    prev = i

def greedy(words):
  line_width = 0
  line = []
  for i in words:
    if (len(i)+line_width)<=total_width:
      line_width = line_width + len(i) + 1
      line.append(i)
    else:
      print(' '.join(line))
      line = []
      line.append(i)
      line_width = len(i) + 1
  print(' '.join(line))

dp=[]
next={}
for i in range(len(words)):
    dp.append(INF)
dp.append(0)

DP(0,dp,next)

print("\n\n   GREEDY JUSTIFICATION")
greedy(words)

print("\n\n   DYNAMIC PROGRAMMING JUSTIFICATION")
justified_text(words,next)
