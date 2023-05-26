#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for linea in sys.stdin:
        columnas = linea.strip().split('\t')
        numero = columnas[0]
        letras = columnas[1]       
        sys.stdout.write("{}\t{}\n".format(numero, letras))