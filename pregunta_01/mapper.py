#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

# Iterar sobre cada línea de entrada
for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en campos
    fields = line.strip().split(',')

    # Comprobar si la línea contiene todos los campos necesarios
    if len(fields) == 21:
        # Obtener el valor del atributo "credit_history"
        credit_history = fields[4]

        # Emitir una clave-valor para el atributo "credit_history"
        print(credit_history + '\t' + '1')