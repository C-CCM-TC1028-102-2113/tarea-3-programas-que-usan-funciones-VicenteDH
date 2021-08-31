def bis (a):
    if (a%4==0 and a%100!=0) or (a%400==0):
        respuesta= 1
    else:
        respuesta= 0
    return respuesta
def main():
    año= int(input())
    z= bis (año)
    if z==1:
        print ("True")
    elif z==0:
        print("False")    
    pass

if __name__=='__main__':
    main()
