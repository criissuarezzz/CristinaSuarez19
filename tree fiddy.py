def LagoNess():
    frase="Siempre va a tratarse de Tree Fiddy"
    if frase.find("Tree Fiddy")!=1: #Si encuentra la palabra Tree Fiddy, y el resultado es distinto de 1, entonces que lo sustituya por 3.50
        search="Tree Fiddy"
        replace="3.50"
        print (frase.replace(search,replace))
    if frase.find("Tree Fiddy")!=-1:
        search="Tree Fiddy"
        replace="three fifty"
        print (frase.replace(search,replace))


if __name__=='__main__':
    LagoNess()