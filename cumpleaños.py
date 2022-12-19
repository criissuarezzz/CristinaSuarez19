dia=input("¿Que día es tu cumpleaños?: ")
mes=input("¿Que mes es tu cumpleaños?: ")
año=input("¿Que año naciste?: ")
def cumpleaños(dia,mes,año):
    for i in range(mes):
        if mes==1:
            mes="Enero"
        elif mes==2:
            mes="Febrero"
        elif mes==3:
            mes="Marzo"
        elif mes==4:
            mes="Abril"
        elif mes==5:
            mes="Mayo"
        elif mes==6:
            mes="Junio"
        elif mes==7:
            mes="Julio"
        elif mes==8:
            mes="Agosto"
        elif mes==9:
            mes="Septiembre"
        elif mes==10:
            mes="Octubre"
        elif mes==11:
            mes="Noviembre"
        elif mes==12:
            mes="Diciembre"
    if dia in range(1,31) and mes in range(1,12) and año in range(1,2022):
        return "Tu cumpleaños es el "+str(dia)+"/"+str(mes)+"/"+str(año), "Tienes "+str(2019-año)+" años".
    if año in range(1944,2000):
        return "Estás en la edad para trabajar"
    elif año in range(1999,2022):
        return "Estás estudiando"
    elif año in range(1,1943):
        return "Estás jubilado"
    else:
        return "No has nacido aún"
