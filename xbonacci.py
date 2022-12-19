#xbonacci sequence
import random, unittest

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
class testxbonacci(unittest.TestCase):
    def testxbonacci(self):
        self.assertEqual(xbonacci(firma,n))


if __name__=='__main__':
    xbonacci(firma,n)
    unittest.main()
    print("La secuencia es correcta")

        
    