base=float(input("Dame la base: "))
altura=float(input("Dame la altura: "))
def main(base,altura):
    area=base*altura
    return(area)
respuesta=main(base,altura)
print("El área del rectángulo es: "+str(respuesta))
