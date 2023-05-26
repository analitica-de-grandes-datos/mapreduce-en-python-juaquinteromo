#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from statistics import mean
import sys
if __name__ == '__main__':
    curkey = None
    lista_valores = []
    for linea in sys.stdin:
        key, val = linea.split("\t")
        val = float(val)        
        if key == curkey:
            lista_valores.append(val)
        else:
            if curkey is not None:
                suma = sum(lista_valores)
                promedio = mean(lista_valores)
                lista_valores.clear()                
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, promedio))
            curkey = key
            lista_valores.append(val)               
    suma = sum(lista_valores)
    promedio = mean(lista_valores)
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, promedio))