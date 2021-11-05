#Simon Christianson Programmed this file
#The date when this was made is 1/26/2021
#The Name of this File is Calculator.py
#This pragram asks the user what calculation the user wants to do (mult, divide, add, or subtract).  It then will output of what the user selects along with the numbers to select
#The variable A throughout this program will be used to reference different spots in the array
Run = True

while Run == True:
    Error = True

    CalcType = input("Please select an option: add/subtract/multiply/divide:")
    CalcType = CalcType.lower()
    if CalcType == "subtract":
        print("NOTE #1 will be the number you subtract from")

    if CalcType == "divide":
        print("NOTE #1 will be the number you divide from")

    if CalcType == "add" or CalcType == ("subtract") or CalcType == ("multiply") or CalcType == ("divide"):
        Error = False

    while Error == True:

        CalcType = input("INVALID ENTRY!  Please selct an option: add/subtract/multiply/divide:")

        if CalcType == "add" or CalcType == ("subtract") or CalcType == ("multiply") or CalcType == ("divide"):
            Error = False
        else:
            Error = True

    print("You chose " + CalcType + ".")

    Numbers = []

    N = int(input("How many numbers would you like to calculate? "))
    for i in range(0,N):
        AskInput = True
        while AskInput == True:
            list = (input("What does #" + str(i+1) + " = "))
            if list.isnumeric():
                AskInput = False

        Numbers.append(list)

    Symbol = "+"
    A = -1
    Answer = 0
    if CalcType == "add":
        while A <N-1:
            A = A+1
            Answer = Answer + float(Numbers[A])

    elif CalcType == "subtract":
        Symbol = "-"
        Z = float(Numbers[0])
        A = 0
        while A <N-1:
            Answer = Z - float(Numbers[A + 1])
            Z = Answer
            A = A + 1
    elif CalcType == "multiply":
        Answer = 1
        Symbol = "*"
        while A <N-1:
            A = A +1
            Answer = float(Answer) * float(Numbers[A])

    else:
        #A = int(Numbers[0])
        Symbol = "/"
        Z = float(Numbers[0])
        A = 0
        while A <N-1:
            Answer = Z / float(Numbers[A + 1])
            Z = Answer
            A = A + 1

    A = -1
    while A < N-1:
            A = A + 1
            print(Numbers[A], end= "")
            #A = A + 1
            if A < N-1:
                print("",Symbol, end=" ")
            if A == N-1:
                print(" =",end=" ")
    print(Answer)
    

    RunAgain = input("Whould you like to calculate something else? (y or n)")
    if RunAgain.lower() == "y" or RunAgain.lower() == "yes":
        Run = True
    else:
        Run = False










