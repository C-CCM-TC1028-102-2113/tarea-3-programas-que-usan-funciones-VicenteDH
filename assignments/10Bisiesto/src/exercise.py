def bis(a):
    if (a%4==0 and a%100==0) or (a%400==0):
        b=1
    else:
        b=0
    return b

def main():
    año=int(input())
    c=bis(año)
    if c==1:
      print("True")
    elif c==0:
        print("False")
    pass


if __name__ == '__main__':
    main()
