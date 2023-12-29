from Bio import SeqIO
from Bio.Seq import complement

palindromes=[]
match_loc=[]
match_len=[]

for seq_record in SeqIO.parse('rosalind_revp.txt', 'fasta'):
    seq_record=seq_record.seq
    seq=seq_record

complement= str(seq.complement())
seq=str(seq)

for i in range (0,len(seq)-1):
    for j in range(i,len(seq)):
        f1=seq[i:j+1]
        
        if len(f1)>=4 and len(f1)<=12:
            
            if f1==complement[i:j+1][::-1]:
                a=(i+1)
                b=(len(f1))
                
                if a not in match_loc:
                    match_loc.append(a)
                    match_len.append(b)
                    
                else:
                    popped=match_len.pop(-1)
                    match_len.append(b)

                
palindromes=list(zip(match_loc,match_len))

for x in palindromes:
    x=str(x)
    x=x.strip('(')
    x=x.strip(')')
    x=x.replace(',','')
    print (x)
