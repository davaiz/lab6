inp = open("input.txt",r) 
otp = open("output.txt",w) 
N = int(inp.readline())
A = inp.readline().split()
k = 0
L = 0
for i in range(N):
    i = int(A[i])
    if i == 5:
        k += 1
    else:
        if (i-5)//5 > k:
            L += (i-5)//5 - k
            k = 0
        else:
            k -= (i-5)//5
otp.write(str(L))
inp.close()
otp.close()


     
    
