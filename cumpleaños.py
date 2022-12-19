from datetime import datetime
print("Hoy es", datetime.today())


dia=int(input("¿Que día es tu cumpleaños?: "))
mes=int(input("¿Que mes es tu cumpleaños?(en número): "))
año=int(input("¿Que año naciste?: "))
fechahoy=datetime.today()
def cumpleaños(dia,mes,año):
    if dia in range(1,31) and mes in range(1,12) and año in range(1,2022):
        print("Tu cumpleaños es el "+str(dia)+"/"+str(mes)+"/"+str(año), "Tienes "+str(2022-fechahoy.year)+" años")
        print("El día de hoy es el "+str(fechahoy.day)+"/"+str(fechahoy.month)+"/"+str(fechahoy.year))
    if año in range(1944,2000):
        print("Estás en la edad de trabajar")
        #Sabemos que un año son 365 días, es decir 52 semanas y 1 día, queremos calcular los lunes que van a pasar desde el día que empezaste a trabajar hasta que te jubiles
        #Los del 2000 se jubilarán en 2078, y los del 1944 en 2022
        #sabemos entonces que hay que trabajar 56 años, (78-22) y que hay que calcular los lunes que van a pasar desde el día que empezaste a trabajar hasta que te jubiles
        
        print(365*56, "días de trabajo, desde los 22 hasta los 78 años")
        edad=fechahoy.year-año #años vividos
        añost=78-22 #años que se van a trabajar
        trabajados=edad-22
        print(añost-trabajados, "años que te quedan por trabajar")
        quedan=365*(añost-trabajados)
        print(quedan, "días que te quedan por trabajar")
        print(quedan/7, "semanas que te quedan por trabajar")
        print(quedan/7/7, "lunes que te quedan por trabajar")
    else:
        print("No tienes edad para trabajar") 
    

if __name__=='__main__':
    cumpleaños(dia,mes,año)
