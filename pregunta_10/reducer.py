#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    diccionario_letras = dict()
    for linea in sys.stdin:        
        numero, letras = linea.split("\t")
        letras = letras.strip().split(",")
        for i in letras:
            if i not in diccionario_letras.keys():
                diccionario_letras[i] = numero
            else:
                diccionario_letras[i] = diccionario_letras[i] + ',' + numero         
        tupla_letras = sorted(diccionario_letras.items(), key=lambda x: x[0])
    for letras, numero_agrupado in tupla_letras:        
        numero_desordenados = numero_agrupado.split(",") 
        numero_ordenados = sorted(numero_desordenados, key=int)
        numero_ordenados = ",".join(numero_ordenados)
        sys.stdout.write("{}\t{}\n".format(letras, numero_ordenados))