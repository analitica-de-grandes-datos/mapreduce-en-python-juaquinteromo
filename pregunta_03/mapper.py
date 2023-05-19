#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#


import sys
if __name__ == "__main__":
    for linea in sys.stdin:
        columnas = linea.split(",")
        if len(columnas) >= 2:
        columna_letra = columnas[0]
        columna_numero = columnas[1]
        sys.stdout.write(f"{columna_letra}\t{columna_numero}\n")
