#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == '__main__':
# Iterar sobre cada línea de entrada
    for linea in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en campos
        campos = linea.split(',')
        campos_credit = campos[2]
        sys.stdout.write(f"{campos_credit}\n")
#
    