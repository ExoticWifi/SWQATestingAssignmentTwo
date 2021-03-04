import math

def menu(arg = 0, testMode = False):
    welcomeMessage()
    #This tells the function if we need the program to request user input
    if testMode == True:
        while True:
            if arg == 1:
                result = 5
                return result
            elif arg == 2:
                result = 3
                return result
            elif arg == 3:
                print("Goodbye!")
                return 2
            else:   
                print("Please make a selecion of either 1, 2, or 3")
                return 1
    else:
        while True:
            userInput = arg
            if userInput == 0:
                arg = int(input())
                userInput = arg
            elif userInput == 1:
                result = bmi()
                arg = 0
            
            elif userInput == 2:
                result = retirement()
                arg = 0
            elif userInput == 3:
                print("Goodbye!")
                break
            else:
                print("Please make a selecion of either 1, 2, or 3")
                arg = 0

        
def bmi(args = [0,0,0], testMode = False):
    #Initialize higher local variables
    weight  = 0
    heightFT = 0
    heightIn = 0

    #tells the program if it needs to request user input
    if testMode == False:
        weight = input("Please enter your weight in lbs as an integer: ")
        heightFT = input("Please enter the amount of feet you are as an integer. For example, if you are 5'10\", enter 5: ")
        heightIn = input("Please enter the amount of inches reamining as an integer. For example, if you are 5'10\", enter 10: ")
    else:
        weight = args[0]
        heightFT = args[1]
        heightIn = args[2]

        
    #weight input validation
    if (testInt(weight) == False):
        print("Invalid weight,", weight, ": Please enter only an integer. No letters please!")
        return False
    if(int(weight) < 0):
        print("Invalid weight,", weight, ": Please enter a weight greater than or equal to 0!")
        return False

    #foot height input validation
    if (testInt(heightFT) == False):
        print("Invalid foot height", heightFT, ": Please enter only an integer. No letters please!")
        return False
    if (int(heightFT) < 0):
        print("Invalid foot height", heightFT, ": Please enter a foot height of greater than or equal to 0")
        return False

    #inches height input validation
    if (testInt(heightIn) == False):
        print("Invalid inch height", heightIn, ": Please enter only an integer. No letters please!")
        return False
    if (int(heightIn) < 0):
        print("Invalid inch height", heightIn, ": Please enter an inch height of greater than or equal to 0")
        return False
    if (int(heightIn) >= 12):
        print("Invalid inch height", heightIn, ": Too many inches! Please add one to your foot height and subtract the amount of inches by 12")
        return False
    
    #changes input types to ints
    weight = int(weight)
    heightFT = int(heightFT)
    heightIn = int(heightIn)

    #bmi calculations
    metricWeight = weight * 0.45
    totalHeightIN = (heightFT * 12) + heightIn
    metricHeight = totalHeightIN * 0.025
    metricHeight = metricHeight * metricHeight
    bmi = round(metricWeight / metricHeight)
    print("Your BMI is: " , bmi)
    welcomeMessage()
    return bmi
    

    
#int tester for input validation
def testInt(i):
    try:
        int(i)
    except ValueError:
        return False


def retirement(args = 0, testMode = False):
    #setting higher local variables
    age = 0
    salary = 0
    percentSaved = 0
    employerMatch = .35
    goal = 0
    ageCap = 100

    #This tells the function if we need the program to request user input
    if testMode == True:
        age = args[0]
        salary = args[1]
        percentSaved = args[2]
        goal = args[3]
    else:
        age = input("Enter your current age as an integer: ")
        salary = input("Enter your current salary as an integer with no commmas/decimals. For example, if $50,000, enter 50000: ")
        percentSaved = input("Enter the percentage amount you would like to save. For example, if 25%, enter 25: ")
        goal = input("Enter your goal amount of money saved as an integer. For example, if $1,000,000, enter 1000000: ")
    
    #age input validation
    if testInt(age) == False:
        print("Invalid Age, ", age, ": Please enter your age as an integer")
        return False
    elif int(age) < 0:
        print("Invalid Age, " , age, ": Please enter your age that is greater than 0")
        return False
    elif int(age) >= 100:
        print("Invalid Age, ", age , ": Please enter an age that is less than 100")
        return False

    #salary input validation
    if testInt(salary) == False:
        print("Invalid salary, " , salary, ": Please enter a salary as an integer with not commas or decimals")
        return False
    elif int(salary) <= 0:
        print("Invalid salary, " , salary, ": Please enter a salary that is greater than 0")
        return False
    
    #savings percentage validation
    if testInt(percentSaved) == False:
        print("Invalid percentage, ", percentSaved, ": Please enter a percent as an integer, for example, if 25%, enter 25")
        return False
    elif int(percentSaved) <= 0:
        print("Invalid percentage, ", percentSaved, ": Please enter a percent greater than 0")
        return False
    elif int(percentSaved) > 100:
        print("Invalid percentage, ", percentSaved, ": Please enter a percent less than 100")
        return False

    #goal input validation
    if testInt(goal) == False:
        print("Invalid goal, ", goal, ": Please enter a goal as an integer, for example, if $1,000,000, enter 1000000")
        return False
    elif int(goal) <= 0:
        print("Invalid goal, ", goal, ": Please enter a goal that is greater than 0")
        return False
    
    #chainging inputs from strings to ints
    age = int(age)
    salary = int(salary)
    percentSaved = int(percentSaved) / 100
    goal = int(goal)

    #retirement calculations
    salaryPercent = salary * percentSaved
    employerPercent = salaryPercent * employerMatch
    saveInstallment = salaryPercent + employerPercent
    amountYears = math.ceil(goal / saveInstallment)
    endAge = age + amountYears
    
    #check to see if one can meet the goal
    if endAge >= 100:
        print("You will not reach your goal")
        welcomeMessage()
        return True
    else:
        print("You will reach your goal at age: ", endAge)
        welcomeMessage()
        return endAge


def welcomeMessage():
    print("Hello! Please select what you would like to do: ")
    print("1: Calculate BMI \n2: Calculate Retirement \n3: Quit")

    

if __name__ == '__main__':
    menu()
