inWallet = 500
inBank = 0
print("--Welcome to the python ATM--")
def askForInputMain():
    inputVar = input("Please select one of the following services: a) Deposit b) Withdrawl c) View amount in bank account d) View amount in wallet ")
    if inputVar == "a" or inputVar == "A" or inputVar == "a)" or inputVar == "A)":
        def askForInputA():
            global inWallet
            global inBank
            inputVar = input("How much would you like to deposit? (you currently have " + str(inWallet) + " in your wallet)")
            inputIsValueA = True
            try:
                inputVar = int(inputVar)
            except ValueError:
                print("Please enter a number")
                inputIsValueA = False
                askForInputA()
            if inputIsValueA == True:
                if inputVar <= inWallet:
                    inBank += inputVar
                    inWallet -= inputVar
                    print("Successfully deposited")
                    askForInputMain()
                else:
                    print("You dont have enough in your wallet")
                    askForInputA()
        askForInputA()
    elif inputVar == "b" or inputVar == "B" or inputVar == "b)" or inputVar == "B)":
        def askForInputB():
            global inWallet
            global inBank
            inputVar = input("How much would you like to withdrawl? (you currently have " + str(inBank) + " in your bank account)")
            inputIsValueB = True
            try:
                inputVar = int(inputVar)
            except ValueError:
                print("Please enter a number")
                inputIsValueB = False
                askForInputB()
            if inputIsValueB == True:
                if inputVar <= inBank:
                    inWallet += inputVar
                    inBank -= inputVar
                    print("Successfully withdrawn")
                    askForInputMain()
                else:
                    print("You dont have enough in your bank account")
        askForInputB()
    elif inputVar == "c" or inputVar == "C" or inputVar == "c)" or inputVar == "C)":
        print("You currently have " + str(inBank) + " in your bank account")
        askForInputMain()
    elif inputVar == "d" or inputVar == "D" or inputVar == "d)" or inputVar == "D)":
        print("You currently have " + str(inWallet) + " in your wallet")
        askForInputMain()
askForInputMain()
