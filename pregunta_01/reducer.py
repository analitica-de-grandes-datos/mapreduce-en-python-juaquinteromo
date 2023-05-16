#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
current_count = 0

# Iterar sobre cada línea de entrada
for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en clave y valor
    key, value = line.strip().split('\t')

    # Convertir el valor en entero
    count = int(value)

    # Si la clave es la misma que la anterior, sumar el valor
    if key == current_key:
        current_count += count
    else:
        # Si la clave es diferente, imprimir la clave anterior y su conteo
        if current_key:
            print(current_key + '\t' + str(current_count))

        # Actualizar la clave y el conteo
        current_key = key
        current_count = count

# Imprimir la última clave y su conteo
if current_key:
    print(current_key + '\t' + str(current_count))