#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for linea in sys.stdin:
        columnas = linea.strip().split('   ')
        fecha = columnas[1]
        fecha_separada = fecha.split('-')
        mes = fecha_separada[1]
        sys.stdout.write("{}\t1\n".format(mes))
