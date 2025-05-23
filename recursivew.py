
def duration():
    w = input("Input initial weight: ")
    w = float(w)
    d = input("Input loss duration: ")
    print(w)
    c = 0
    for i in range (int(d)):
        p = w*.01
        w = w - p
        print("Week: " + str(i+1+(c*8)) + " Weight: " +"{:.2f}".format(w))
        if (i+1)%12 == 0:
            c = c + 1
            print("Maintenance Period: + 8 Weeks")
    menu()
    
def goal():
    w = input("Input initial weight: ")
    w = float(w)
    g = input("Input goal weight: ")
    g = int(g)

    i = 0
    while w > g:
        p = w*.01
        w = w - p
        i = i + 1

    print("Weeks to target: " + str(i))
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
menu()
