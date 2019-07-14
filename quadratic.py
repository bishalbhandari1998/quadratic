def alpha():
    a=float(input("please enter the coefficient of x^2 term"))
    b=float(input("please enter the coefficient of x term"))
    c=float(input("please enter the value of the constant "))

    formula=(-b+(b**2-(4*a*c))**0.5)/2
    formula1=(-b-(b**2-(4*a*c))**0.5)/2
    if ((b**2)-(4*a*c))<0:
        print("no real roots")
    else:
        print(" your roots are", formula1, "and",formula)
    restart= input("do youi wanna do it again").capitalize()
    if restart == "No":
        exit()
    if restart == "Yes":
        alpha()
alpha()