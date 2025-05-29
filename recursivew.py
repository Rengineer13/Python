
def duration():
    while True:
        try:
            w = input("Input initial weight: ")
            w = float(w)
            d = input("Input loss duration: ")
            d = int(d)
            per = input("Input percentage weight loss (between 0 and 1): ")
            per = float(per)
            if(per > 1):
                print("WARNING!! You have selected a weight loss percentage above 1%. This is NOT recommended!")
        except ValueError:
            print("One or more of your inputs is not valid, please try again.")
        else:
            break
    print(w)
    c = 0
    init_w = w
    for i in range (int(d)):
        p = w*(per/100)
        w = w - p
        print("Week: " + str(i+1+(c*8)) + " Weight: " +"{:.2f}".format(w)+ " Weekly Loss: " + "{:.2f}".format(p) + " Daily Loss: " + "{:.2f}".format(p/7))
        if (i+1)%12 == 0:
            c = c + 1
            print("Total weight lost: " + "{:.2f}".format(init_w - w))
            print("Maintenance Period: + 8 Weeks")
            init_w = w
        elif (i+1 == int(d)):
            print("Total weight lost: " + "{:.2f}".format(init_w - w))
    menu()
    
def goal():
    while True:
        try:
            w = input("Input initial weight: ")
            w = float(w)
            per = input("Input percentage weight loss (between 0 and 1): ")
            per = float(per)
            if(per > 1):
                print("WARNING!! You have selected a weight loss percentage above 1%. This is NOT recommended!")
            g = input("Input goal weight: ")
            g = int(g)
        except ValueError:
            print("One or more of your inputs is not valid, please try again.")
        else:
            break

    i = 0
    c = 0
    init_w = w
    while w > g:
        p = w*(per/100)
        w = w - p
        i = i + 1
        
        if (i+1)%12 == 0:
            c = c + 1
    print("Weeks to target: " + str(i))
    print("Weeks of maintenance: " + str(c*8))
    print("Total time: " + str((c*8)+i))
    choice = input("Calculate plan? (Y/N)")
    match choice:
        case "Y":
                w = init_w
                c = 0
                print("Initial Weight: " + str(w))
                for x in range (i):
                    p = w*(per/100)
                    w = w - p
                    print("Week: " + str(x+1+(c*8)) + " Weight: " +"{:.2f}".format(w)+ " Weekly Loss: " + "{:.2f}".format(p) + " Daily Loss: " + "{:.2f}".format(p/7))
                    if (x+1)%12 == 0:
                        c = c + 1
                        print("Total weight lost: " + "{:.2f}".format(init_w - w))
                        print("Maintenance Period: + 8 Weeks")
                        init_w = w
                    elif (x+1 == i):
                        print("Total weight lost: " + "{:.2f}".format(init_w - w))
                menu()
        case "N":
            menu()
        case _:
            print("Invalid selection, returning to menu")
            menu()

def menu():
    choice = input("Type d for duration, g for goal, e for exit: ")
    match choice:
        case "d":
            duration()
        case "g":
            goal()
        case "e":
            return
        case _:
            print("Invalid choice!")
            menu()
menu()
