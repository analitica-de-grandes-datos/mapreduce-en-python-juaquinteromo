#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for linea in sys.stdin:
        columnas = linea.strip().split('   ')
        letras = columnas[0]
        valor = columnas[2]        
        sys.stdout.write("{}\t{}\n".format(letras, valor))