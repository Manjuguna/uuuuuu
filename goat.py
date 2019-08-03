def sb(root): 
    mud = len(root) 
    sb = [1]*mud 
    for i in range (1 , mud): 
        for j in range(0 , i): 
            if root[i] > root[j] and sb[i]< sb[j] + 1 : 
                sb[i] = sb[j]+1
    maximum = 0
    for i in range(mud): 
        maximum = max(maximum , sb[i])  
    return maximum
ars=int(input()) 
root = list(map(int,input().split()))
print (sb(root))
