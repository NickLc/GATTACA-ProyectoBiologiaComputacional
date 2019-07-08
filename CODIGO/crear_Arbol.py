# 2. Leer las secuencias alineadas 
from Bio import AlignIO

def leer_SecAli(input_clustal = 'data_gen/Sec_Alineadas.clustal'):

	""" Recibe la direccion del archivo clutal con la secuencias aliendas 
		Retorna un objeto alineamiento"""
	#input_clustal = 'data_gen/Sec_Unidas.clustal'
	aln = open(input_clustal, "r")
	#usar AlignIO tpara leer el archivo de alineamiento en formato 'clustal' format
	alignment = AlignIO.read(aln, "clustal")
	return alignment

#========================================================================
# 4. Creamos el arbol UPGMA a partir de la matriz
from Bio.Phylo.TreeConstruction import DistanceCalculator  # crear la matriz de distancias
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

def create_Tree(alignment, tipo = 'upgma'):
	"""Se recibe de entrada el alimenamiento y el tipo de arbol nj o upgma 
	Genera el arbol filogenetico 
	"""
	print('Creando el arbol filogenetico ......')
	# 3. Creamos la matriz de distancias
	calculator = DistanceCalculator('identity')
	# añade la matriz de  distancias al objeto calculator y lo retorna
	dm = calculator.get_distance(alignment)

	#initialize a DistanceTreeConstructor object based on our distance calculator object
	constructor = DistanceTreeConstructor(calculator)
	
	#build the tree
	if tipo == 'upgma':
		tree = constructor.upgma(dm)
	if tipo == 'nj':
		tree = constructor.nj(dm)

	return tree

#========================================================================
# __Mostrar el arbol__

from Bio import Phylo
import pylab

def draw_Tree(tree):
	""" Muestra el arbol en pantalla"""
	Phylo.draw(tree)
