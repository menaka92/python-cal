while True:
    print("Select operation.")
    print("1.Add: + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide : / ")
    print("5.Power: ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset: $ ")
    
    a = float(input("Enter 1st number: "))
    b  = float(input("Enter 2nd number: "))
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")

    def add(a,b):
        return(a+b)
    def sub(a,b):
        return(a-b)
    def multy(a,b):
        return(a*b)
    def dev(a,b):
        if(b==0):
            print("Not a valid number,please enter again")
            return None
        else:
            return(a/b)
    def power(a, b):
        return a ** b
    def remainder(a, b):
        if b == 0:
            print("Not a valid number,please enter again")
            return None
        else:
            return (a % b)

    if(choice=='+'):
        print (add(a,b))
    if(choice=='-'):
        print (sub(a,b))
    if(choice=='*'):
        print (multy(a,b))
    if(choice=='/'):
        print (dev(a,b))
    if(choice=='^'):
        print (power(a,b))
    if(choice=='%'):
        print (remainder(a,b))
    if(choice=='#'):
        break
    if(choice=='$'):
        continue
