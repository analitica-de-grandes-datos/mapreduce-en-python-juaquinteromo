#
# >>> Escriba el codigo del reducer a partir de este punto <<<
import sys
if _name_ == "_main_":
    atributo = {}
    for linea in sys.stdin:
        campos = linea.split("\n")
        campos_credit = campos[0]
        if campos_credit in atributo:
            atributo[campos_credit] += 1
        else:
            atributo[campos_credit] =1
    atributo_sort = sorted(atributo.items())
    for atributo,valor in atributo_sort:
        sys.stdout.write(f"{atributo}\t{valor}\n")
        