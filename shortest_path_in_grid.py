matrix = []
row = int(input('Enter the number of rows : '))
col = int(input('Enter the number of collumns : '))

print('Enter matrix : ')
for i in range(row):
  r = list(map(int,input('Enter row {} : '.format(i)).strip().split()))[:col]
  matrix.append(r)

m = int(input('Enter the destination row index : '))
n = int(input('Enter the destination col index : '))

assert(m<row and m>=0 and n<col and n>=0)

def minimum(matrix,parent,i,j,m,n):
  min = float('inf')
  index = -1
  if i+1<=m: 
    min = DP(matrix,parent,i+1,j,m,n)
    index = 1
  x = DP(matrix,parent,i,j+1,m,n)
  if x<min and j+1<=n:
    min = x
    index = 2
  x = DP(matrix,parent,i+1,j+1,m,n)
  if x<min and i+1<=m and j+1<=n:
    min = x
    index = 3
  return min,index

def DP(matrix,parent,i,j,m,n):

  if i==m and j==n:
    return matrix[i][j]

  if i>m or j>n:
    return float('inf')

  if parent[i][j]!=-1:
    return matrix[i][j]

  cost,x = minimum(matrix,parent,i,j,m,n)
  parent[i][j] = x
  matrix[i][j] = matrix[i][j] + cost
  return matrix[i][j]

def reconstruct(parent,m,n,i=0,j=0):
  s = []
  while parent[i][j]!=-1 and i<=m and j<=n:
    s.append('({},{})'.format(i,j))
    if parent[i][j] == 1:
      i+=1
    elif parent[i][j] == 2:
      j+=1
    else:
      i+=1
      j+=1
  if i==m and j==n:
    s.append('({},{})'.format(i,j))
    print('->'.join(s))
  else:
    print('NO SOLN')
  return

parent = []
for i in range(row):
  y = []
  for j in range(col):
    y.append(-1)
  parent.append(y)
min_cost = DP(matrix,parent,0,0,m,n)
print('PATH : ')
reconstruct(parent,m,n)
print('MIN COST : {}'.format(min_cost))