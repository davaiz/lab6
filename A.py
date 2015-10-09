input = open('input.txt', 'r')
output = open('output.txt', 'w')
N = int(input())
A = list(map(int, input().split()))
for i in A: 
    if A.count(i) == 2:
        pritn(i, file=output)
        break

      