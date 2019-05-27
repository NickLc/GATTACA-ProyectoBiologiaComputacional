from Bio_Tool import *

#if __name__ == 'prueba.py':
elegidos = [0,1,2,6,8,9,10]
join_Fasta(elegidos)
alinear_Secuencias()
aln = leer_SecAli()
print("\nLas secuencias alineadas son\n",aln)
tree = create_Tree(aln, tipo = 'nj')
draw_Tree(tree)
save_Tree(tree)