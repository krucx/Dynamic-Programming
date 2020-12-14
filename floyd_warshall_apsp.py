adj_matx = []
V = int(input('Enter the number of vertices : '))
for i in range(V):
  adj_matx.append(list(input().strip().split())[:V])

for i in range(V):
  for j in range(V):
    if adj_matx[i][j] == 'INF':
      adj_matx[i][j] = float('inf')
    else:
      adj_matx[i][j] = int(adj_matx[i][j])

def floyd_warshall(dist,next,V):
  for k in range(V):
    for u in range(V):
      for v in range(V):
        if dist[u][v] > dist[u][k] + dist[k][v]:
          dist[u][v] = dist[u][k] + dist[k][v]
          next[u][v] = next[u][k]

def print_paths(dist,next,V):
  for u in range(V):
    for v in range(V):
      s = []
      k = next[u][v]
      s.append(str(u))
      while k!=v:
        if k==-1:
          print('NO PATH EXISTS')
          break
        s.append(str(k))
        k = next[k][v]
      if k==v:
        s.append(str(v))
        print('SHORTEST PATH FROM {} to {} WITH DISTANCE : {}'.format(u,v,dist[u][v]))
        print('->'.join(s))
        print('__________________________________________________')

next = []
for i in range(V):
  row = []
  for j in range(V):
    if adj_matx[i][j]!=float('inf'):
      row.append(j)
    else:
      row.append(-1)
  next.append(row)
dist = [row[:] for row in adj_matx]
floyd_warshall(dist,next,V)
print_paths(dist,next,V)