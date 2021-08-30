def main(base,profundidad):
    arect=base*profundidad
    return (arect)

def vol(area,altura):
    cal=area*altura
    return(cal)

base=float(input("Dame la base: "))
altura= float(input("Dame la altura: "))
profundidad=float(input("Dame la profundidad: "))
area=main(base, profundidad)
volumen=vol(area,altura)
print("El volumen del prisma es: "+str(volumen))
