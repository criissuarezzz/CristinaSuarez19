h=int(input("¿De qué altura quieres el triángulo?: "))

def hollow_triangle(h):
    for i in range(h):
        for j in range(h-i):
            print("", end="")  #Para generear espacios en blanco
        
        for j in range (2*i+1):
            if j==0 or j==2*i or i==h-1:   #Para que genere los bordes del triángulo
                print("#", end="")
            elif j==h:   #Para que cuando h coincida con la última línea la complete con #
                print("","#", end="")  
            else:
                print(" ", end="")   #Y si no ocurre nada de eso, espacio en blanco
        print()

if __name__=='__main__':
    hollow_triangle(h)