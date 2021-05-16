def add(data, b):
    f = open(b, "a")
    a = f.write(str(getdate()) + ': ' + data + '\n')
    f.close()

def retreive(info):
    f = open(info)
    content = f.read()
    print(content)
    f.close()

def getdate():
    import datetime
    x = datetime.datetime.now()
    return x.strftime("%d/%b/%Y %I:%M %p")


def addexp(fuel):
    f = open(fuel)
    str1 = f.read()
    res = [int(s) for s in str1.split() if s.isdigit()]
    print("You spend total " + str(sum(res)) + "rs")
    f.close()


print("This is Fuel management system developed in python by Syed Muhammad Hussain")
while (True):
    print("Did you want to add, retrieve your data or get sum of your expenses")
    addorret = int(input("Press 1 to add or 2 to retreive or 3 to get sum of expenses \n"))
    name = int(input("Press \n1 for petrol\n2 for Cng\n"))

    if addorret == 1:
        if name == 1:
            ex = input("What update you want add in your petrol management system\n")
            add(ex, "petrol.txt")
            print("You have successfully updated your data in your petrol management system")
            ite = input("Press Enter key to continue or 1 to quit: ")
            if ite == '1':
                break
            else:
                continue
        elif name == 2:
            ex = input("What update you want add in your cng management system\n")
            add(ex, "Cng.txt")
            print("You have successfully updated your data in your cng management system")
            ite = input("Press Enter key to continue or 1 to quit: ")
            if ite == '1':
                break
            else:
                continue
        else:
            print("Please enter valid choice")
            ite = input("Press Enter key to continue or 1 to quit: ")
            if ite == '1':
                break
            else:
                continue
    elif addorret == 2:
        if name == 1:
            retreive("petrol.txt")
            print("You have successfully retreive your data from your petrol management system")
            ite = input("Press Enter key to continue or 1 to quit: ")
            if ite == '1':
                break
            else:
                continue
        elif name == 2:
            retreive("Cng.txt")
            print("You have successfully retreive your data from your cng management system")
            ite = input("Press Enter key to continue or 1 to quit: ")
            if ite == '1':
                break
            else:
                continue
        else:
            print("Enter valid choice")
            ite = input("Press Enter key to continue or 1 to quit: ")
            if ite == '1':
                break
            else:
                continue

    elif addorret == 3:
        if name == 1:
            addexp("petrol.txt")
            ite = input("Press Enter key to continue or 1 to quit: ")
            if ite == '1':
                break
            else:
                continue
        elif name == 2:
            addexp("Cng.txt")
            ite = input("Press Enter key to continue or 1 to quit: ")
            if ite == '1':
                break
            else:
                continue
        else:
            print("Enter valid choice")
            ite = input("Press Enter key to continue or 1 to quit: ")
            if ite == '1':
                break
            else:
                continue
    else:
        print("Enter valid choice")
        ite = input("Press Enter key to continue or 1 to quit: ")
        if ite == '1':
            break
        else:
            continue
