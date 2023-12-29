def utree_number(n):
    even=[]
    odd=[]
    value= 2*n-5
    result=1

    
    for i in range (1,value+1):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
            
    if value%2==0:
        for i in range (len(even)):
            result= result* even[i]
    else:
        for i in range (len(odd)):
            result= result* odd[i]

    print(result%1000000)
    

utree_number(816)