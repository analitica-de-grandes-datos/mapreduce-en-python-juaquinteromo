#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    con_letras = {}
    for line in sys.stdin:
        columnas = line.split("\n")
        letras = columnas [0]
        if letras in con_letras:
           con_letras[letras] += 1
        else:
            con_letras[letras] = 1
    ord_con_letras = sorted(con_letras.items())
    for key,valor in ord_con_letras:
        sys.stdout.write(f"{key},{valor}\n")