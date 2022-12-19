h=int(input("¿De qué altura quieres el triángulo?: "))
def hollow_triangle(h):
    for i in range(h):
        for j in range(h-i):
            print("", end="")
        
        for j in range (2*i+1):
            if j==0 or j==2*i or i==h-1:
                begining="__"
                print(begining="__"+"#", end="__")
            else:
                print(" ", end="")
if __name__=='__main__':
    hollow_triangle(h)