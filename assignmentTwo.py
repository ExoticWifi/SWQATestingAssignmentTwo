
def menu(arg = 0, testMode = False):
    print("Hello! Please select what you would like to do: ")
    print("1: Calculate BMI \n 2: Calculate Retirement \n 3: Quit")
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
                arg = int(input("1: Calculate BMI \n2: Calculate Retirement \n3: Quit \n"))
                userInput = arg
            elif userInput == 1:
                result = bmi()
                arg = 0
            elif userInput == 2:
                arg = 0
                result = retirement()
            elif userInput == 3:
                print("Goodbye!")
                break
            else:
                print("Please make a selecion of either 1, 2, or 3")
                arg = 0

        
def bmi(args = [0,0,0], testMode = False):
    weight  = 0
    heightFT = 0
    heightIn = 0

    if testMode == False:
        weight = input("Please enter your weight in lbs: ")
        heightFT = input("Please enter the amount of feet you are: ")
        heightIn = input("Please enter the amount of inches reamining: ")
    else:
        weight = args[0]
        heightFT = args[1]
        heightIn = args[2]

    if (testInt(weight) == False):
        print("Invalid weight: Please enter only an integer. No letters please!")
        return False
    
    if (testInt(heightFT) == False):
        print("Invalid foot height: Please enter only an integer. No letters please!")
        return False

    if (heightFT < 0):
        print("Invalid foot height: Please enter a foot height of greater than or equal to 0")
        return False
    
    if (testInt(heightIn) == False):
        print("Invalid inch height: Please enter only an integer. No letters please!")
        return False
    
    if (heightIn < 0):
        print("Invalid inch height: Please enter an inch height of greater than or equal to 0")
        return False
    
    if (heightIn >= 12):
        print("Invalid inch height: Too many inches! Please add one to your foot height and subtract the amount of inches by 12")
        return False
    
    metricWeight = weight * 0.45
    totalHeightIN = (heightFT * 12) + heightIn
    metricHeight = totalHeightIN * 0.025
    metricHeight = metricHeight * metricHeight
    bmi = round(metricWeight / metricHeight)
    print("Your BMI is: " , bmi)
    return bmi
    

    
    
def testInt(i):
    try:
        int(i)
    except ValueError:
        return False

def retirement(args = 0, testMode = False):
    print("Retirement")
    #return 3

if __name__ == '__main__':
    menu()
