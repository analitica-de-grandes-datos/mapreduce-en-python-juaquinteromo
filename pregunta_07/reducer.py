#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    lista_tuplas = []    
    for linea in sys.stdin:
        key, fecha, valor = linea.split("\t")
        valor = int(valor)
        tuple = (key, fecha, valor)
        lista_tuplas.append(tuple)        
    lista_tuplas = sorted(lista_tuplas, key=lambda x: (x[0],x[2]))
    for tuple in lista_tuplas:
        sys.stdout.write("{}   {}   {}\n".format(tuple[0], tuple[1], tuple[2]))
    