#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    lista_tuplas = []
    for linea in sys.stdin:
        key, fecha, valor = linea.split("\t")
        valor = int(valor)
        tupla = (key, fecha, valor)
        lista_tuplas.append(tupla)       
    lista_tuplas = sorted(lista_tuplas, key=lambda x: x[2])
    tuplas_conjunto = lista_tuplas[0:6]
    for tuple in tuplas_conjunto:
        sys.stdout.write("{}   {}   {}\n".format(tuple[0], tuple[1], tuple[2]))