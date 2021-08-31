papel=int(input("Dame la cantidad de pliegos de papel albanene: "))
plumones=int(input("Dame la cantidad de plumones: "))
def main(papel,plumones):
    total1=papel*12
    total2=plumones*35
    if total1>total2:
        return("El número máximo de tarjetas que se pueden hacer es: "+str(total1))
    elif total2>total1:
        return("El número máximo de tarjetas que se pueden hacer es: "+str(total2))
resultado=main(papel,plumones)    
print(resultado)
