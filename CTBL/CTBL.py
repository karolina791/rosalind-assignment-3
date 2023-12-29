from Bio import Phylo

tree=Phylo.read('rosalind_ctbl.txt','newick')

taxa=sorted([taxon.name for taxon in tree.get_terminals() if taxon!= None])
root= tree.root

def print_row(clade, root):
    on=[]
    off=[]
    row=''
    nodes = set(tree.root.get_terminals())
    on= [i.name for i in set(clade.get_terminals())]
    off= [i.name for i in nodes - set(clade.get_terminals())]
    
    for taxon in taxa:
        if taxon in on:
            row+='1'
        elif taxon in off:
            row+='0'
    print(row)  
    
def terminal(clade, root):
    for pos in clade.clades:
        if not pos.is_terminal():
            print_row(pos, root)
            terminal(pos, root)

terminal(root, root)