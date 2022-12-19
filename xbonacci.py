#xbonacci sequence
import random

n=int(input("¿Cuántos números quieres como firma de la secuencia?: "))
firma=[]
for i in range(n):
    firma.append(random.rrandint(0,1))
def xbonacci(firma, n):
    if n==0:
        return []
    if n==1:
        return firma[0]