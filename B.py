k=0 
L=0 
input=open('input.txt','r') 
output=open('output.txt','w') 
n=int(input.readline()) 
a=input.readline().split() 
for i in range(n): 
    kup=int(a[i]) 
    kup=(kup-5)//5 
    if kup==0: 
        k-=1 
    elif kup<(-k): 
        k+=kup 
    else:  
        L+=k+kup
        k=0 
print(l,file=output) 

     
    
