#./clustalo -i globin.fa -o globin.aln --outfmt=clu --force

import os
def alinear_Secuencia(filename):
    dir_inicio='data_gen'
    dir_final = 'Clustal_Omega'
    salida_ali = 'Sec_Alineadas.clustal'
    
    mover_archivo(dir_inicio, dir_final, filename)
    #Realizar el alineamiento
    comando = 'cd Clustal_Omega & clustalo.exe -i {} -o {} --outfmt=clu --force'.format(filename, salida_ali)
    os.system(comando)
    print('Se genero el archivo: {}'.format(salida_ali))

    mover_archivo(dir_final, dir_inicio, salida_ali)
    mover_archivo(dir_final, dir_inicio, filename)
    
def mover_archivo(dir_inicio, dir_final, filename):
    comando = 'move {}\{} {}\{}'.format(dir_inicio,filename, dir_final, filename)
    os.system(comando)

alinear_Secuencia('Sec_Unidas.fasta')



