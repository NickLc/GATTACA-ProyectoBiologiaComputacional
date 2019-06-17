from Bio_Tool import *
from Bio import Phylo

#if __name__ == 'prueba.py':
elegidos = [1,2,5,9]
join_Fasta(elegidos)
alinear_Secuencias()
aln = leer_SecAli()
#print("\nLas secuencias alineadas son\n",aln)
#tree = create_Tree(aln)
#print(tree)
tree = Phylo.read('data_gen/tree.xml', 'phyloxml')
draw_Tree(tree)
#save_Tree(tree)