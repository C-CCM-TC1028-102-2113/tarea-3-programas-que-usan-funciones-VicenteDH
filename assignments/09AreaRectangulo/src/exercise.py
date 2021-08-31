def main():
    base= float(input("Dame la base: "))
    altura= float(input("Dame la altura: "))
    c=(rect(base,altura))
    print("El área del rectángulo es: "+str(c))
    pass
def rect(b,a):
    area=b*a
    return(area)
if __name__=='__main__':
    main()
