q = 0
inp = open('input.txt','r')
out = open('output.txt','w')
N = int(inp.readline())
A = inp.readline().split()
for i in range(N):
  A[i] = int(A[i])
m = N + 1
for i in range(N):
  if((A[i]) < 0) and (A[i+1:].count(-A[i]) > 0):
    q = A.index(-A[i])-i
    if q < m:
      m = q
if m == n + 1:
  print(0, file=out)
else:
  print(m, file=out)
