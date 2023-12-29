from itertools import permutations


def perm(n):
    numbers=[]

    for i in range (1,n+1):
        numbers.append(i)
        perm_list=list(permutations(numbers,n))
    
    print (len(perm_list))
    
    for j in (perm_list):
        j=str(j)
        j=j.strip('(')
        j=j.strip(')')
        j=j.replace(',','')
        print (j)
       

    
    
    
perm(6)
    
    
    