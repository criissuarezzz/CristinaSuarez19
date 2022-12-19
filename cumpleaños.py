dia=input("¿Que día es tu cumpleaños?: ")
mes=input("¿Que mes es tu cumpleaños?(en número): ")
for i in range(mes):
    if mes=="Enero" or "enero":
        mes=1
    elif mes=="Febrero" or "febrero":
        mes=2
    elif mes=="Marzo" or "marzo":
        mes=3
    elif mes=="Abril" or "abril":
        mes=4
    elif mes=="Mayo" or "mayo":
        mes=5
    elif mes=="Junio" or "junio":
        mes=6
    elif mes=="Julio" or "julio":
        mes=7
    elif mes=="Agosto" or "agosto":
        mes=8
    elif mes=="Septiembre" or "septiembre":
        mes=9
    elif mes=="Octubre" or "octubre":
        mes=10
    elif mes=="Noviembre" or "noviembre":
        mes=11
    elif mes=="Diciembre" or "diciembre":
        mes=12
año=input("¿Que año naciste?: ")
def cumpleaños(dia,mes,año):
    if dia in range(1,31) and mes in range(1,12) and año in range(1,2022):
        return ("Tu cumpleaños es el "+str(dia)+"/"+str(mes)+"/"+str(año), "Tienes "+str(2019-año)+" años")
    if año in range(1944,2000):
        return "Estás en la edad para trabajar"
    elif año in range(1999,2022):
        return "Estás estudiando"
    elif año in range(1,1943):
        return "Estás jubilado"
    else:
        return "No has nacido aún"
print(cumpleaños(dia,mes,año))
