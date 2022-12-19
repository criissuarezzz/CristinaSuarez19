#xbonacci sequence
import random, unittest

n=int(input("¿Cuántos números quieres como firma de la secuencia?: "))
firma=[]
for i in range(n):
    firma.append(random.randint(0,1))  #Para que incluya tantos 0 y 1 a la lista firma como su rango(n) indica
def xbonacci(firma, n):   #Creamos la función xbonacci
    if n==0:
        return []
    for i in range(n):    #Para que la secuencia tenga tantos números como su rango(n) indica
        firma.append(sum(firma[-n:]))   #Añadimos a la lista firma la suma de los últimos n números
    return firma
class testxbonacci(unittest.TestCase):      #test
    def testxbonacci(self):
        self.assertEqual(xbonacci(firma,n))


if __name__=='__main__':
    xbonacci(firma,n)
    unittest.main()
    print("La secuencia es correcta")

        
    