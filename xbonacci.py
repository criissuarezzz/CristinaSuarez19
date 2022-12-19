#xbonacci sequence
import random

n=int(input("¿Cuántos números quieres como firma de la secuencia?: "))
firma=[]
for i in range(n):
    firma.append(random.randint(0,1))
def xbonacci(firma, n):
    if n==0:
        return []
    for i in range(n):
        firma.append(sum(firma[-n:]))
    return firma

if __name__=='__main__':
    print(xbonacci(firma,n))
        
    