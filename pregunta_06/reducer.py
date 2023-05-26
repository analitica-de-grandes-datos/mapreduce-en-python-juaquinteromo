#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    curkey = None
    lista_valores = []
    for linea in sys.stdin:
        key, val = linea.split("\t")
        val = float(val)
        if key == curkey:
            # Se acumulan los valores para la misma key
            lista_valores .append(val)
        else:
            if curkey is not None:
                # Siendo la misma key se obtiene el max y min
                maximo = max(lista_valores)
                minimo = min(lista_valores)
                lista_valores .clear()                
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))
            curkey = key
            lista_valores .append(val)               
    maximo = max(lista_valores)
    minimo = min(lista_valores)
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))