def main():
    base=float(input("Dame la base: "))
    altura= float(input("Dame la altura: "))
    profundidad=float(input("Dame la profundidad: "))
    a= area(base,profundidad)
    c=vol(a,altura)
    print("El volumen del prisma es: "+str(c))
    pass

def area(b,p):
    arect=b*p
    return (arect)

def vol(ar,al):
    cal=ar*al
    return(cal)

if __name__ == '__main__':
    main()
