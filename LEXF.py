
def possible_str(symbols, n):
    from itertools import product 
    symbols=symbols.replace(' ','')
    str_list= list(product(symbols,repeat=n))
    
    
    for i in str_list:
        i=str(i)
        i=i.strip('(')
        i=i.strip(')')
        i=i.replace("'","")
        i=i.replace(", ","")
        
        print (i)
        
        
        
possible_str ("A B C D E F G H", 3)        
