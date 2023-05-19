#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    datos = []
    for line in sys.stdin:
        columnas = line.strip().split("\t")
        columna1 = columnas[0]
        columna2 = int(columnas[1])
        datos.append((columna1,columna2))
    datos= sorted(datos,key=lambda x: x[1])
    
    for item in datos:
        sys.stdout.write(f"{item[0]},{item[1]}\n")

