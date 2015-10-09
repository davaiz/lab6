k = 0 
L = 0 
inp = open('input.txt','r') 
out = open('output.txt','w') 
n = int(inp.readline()) 
a = inp.readline().split() 
for i in range(n): 
    p = int(a[i]) 
    if p == 5: 
        k -= 1 
    elif (p-5)//5  < (-k): 
        k+=(p-5)//5  
    else:  
        L += k + (p-5)//5 
        k = 0 
print(L, file = out)


     
    
