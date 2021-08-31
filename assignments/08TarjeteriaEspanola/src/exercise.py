def main():
    papel=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones=int(input("Dame la cantidad de plumones: "))
    c=tarjeta(papel, plumones)
    print(c)
    pass

def tarjeta(pa,pl):
    total1=pa*12
    total2=pl*35
    if total1<total2:
        return("El número máximo de tarjetas que se pueden hacer es: "+str(total1))
    elif total2<total1:
        return("El número máximo de tarjetas que se pueden hacer es: "+str(total2))

if __name__ == '__main__':
    main()
