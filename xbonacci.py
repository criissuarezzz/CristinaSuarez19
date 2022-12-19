#xbonacci sequence
import random

n=int(input("¿Cuántos números quieres como firma de la secuencia?: "))
firma=[]
for i in range(n):
    firma.append(random.rrandint(0,1))
def xbonacci(firma, n):
    for i in range(n):
        firma.append(sum(firma[-n:]))
    return firma
        
    