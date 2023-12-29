from Bio import SeqIO
    
seq= str((SeqIO.read('rosalind_kmp9.txt','fasta')).seq)
sfail_ar=list(('0')*len(seq))
fail_ar=[]

for i in sfail_ar:
    i=int(i)
    fail_ar.append(i)

for j in range (1,len(seq)):
    k=fail_ar[j-1]
    
    if k>0 and seq[j]!=seq[k]:
        k= fail_ar[k-1]
        
    if seq[j]==seq[k]:
            k+=1
            fail_ar[j]=k


fail_ar=str(fail_ar)
fail_ar=fail_ar.strip('[')
fail_ar=fail_ar.strip(']')
fail_ar=fail_ar.replace(',','')

with open('KMP.txt', 'w') as file:
    file.write(fail_ar)