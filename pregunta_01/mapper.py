#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if _name_ == "_main_":
    for linea in sys.stdin:
        columnas = linea.split(",")
        columna_credit = columnas[2]
        sys.stdout.write(f"{columna_credit}\n")
#
#
    