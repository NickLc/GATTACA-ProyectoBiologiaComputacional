
# coding: utf-8

# # Proyecto Biologia Computacional
from Bio import SeqIO
import os

#========================================================================
# Unir varios archivos fasta

def join_Fasta(elegidos):
	"""Une las secuencias que se encuentran en el directorio input_dir 
	además que se encuentren el la lista de los elegidos = [1,3,4,8]. 
	Retorna en la secuencia total en el directorio output_dir"""
	input_dir = 'data_gen/fasta/' 
	output_dir = 'data_gen/Sec_Unidas.fasta'
	print('Procediendo a leer los ficheros de ', input_dir)
	records = []
	num_seq = -1
	for seq in os.listdir(input_dir):
		num_seq += 1 
		if num_seq in elegidos:
		    fichero = open(input_dir + seq)
		    record = SeqIO.read(fichero, 'fasta')
		    records.append(record)

	print('Escribiendo fichero total...')
	SeqIO.write(records, output_dir, 'fasta')
	print('Finalizado.')

#========================================================================

# 1. Alineamiento de secuencias - Generar el archivo clustal
# MUSCLE
# ClustalW y ClustalW strict original para una máxima compatibilidad

from Bio.Align.Applications import MuscleCommandline
import subprocess

def alinear_Secuencias(tipo='clwstrict'):
	""" Recibe un archivo fasta que contiene todas las secuencias elegidas
	Retorna el alineamiento, el tipo puede ser 'clw' o 'clwstrict'"""
	archivo_fasta = 'data_gen/Sec_Unidas.fasta'
	output = 'data_gen/Sec_Unidas.clustal'
	if tipo == 'clw':
		print("Secuencias alineadas con clw")
		#muscle_cline = MuscleCommandline(input=archivo_fasta, clw=True)
	if tipo == 'clwstrict':
		print("Secuencias alineadas con clwstrict")
		#muscle_cline = MuscleCommandline(input=archivo_fasta, clwstrict=True)

#========================================================================

# 2. Leer la secuencia

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
	Genera ell arbol filogenetico 
	"""

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

#========================================================================
# 6. Grabamos el archivos en formato PhyloXML

import sys
#Grabamos  el arbol UPGMA
def save_Tree(tree, address='data_gen/tree.xml'):
	"""Guardamos el arbol en una direccion del directorio en formato .xml"""
	
	f = open(address, "w") 
	Phylo.write(tree,f,"phyloxml")
	print("Archivo guardado en ",address)
	  

if __name__ == 'Bio_Tool' :
    print("Bio_Tool se ha importado correctamente.")