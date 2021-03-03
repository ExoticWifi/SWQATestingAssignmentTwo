def menu(arg):
    print("Hello! Please select what you would like to do: ")
    print("1: Calculate BMI \n 2: Calculate Retirement \n 3: Quit")
    
    while True:
        input = arg
        if input == 1:
            result = bmi()
            return result
        elif input == 2:
            result = retirement()
            return result
        elif input == 3:
            print("Goodbye!")
            return 2
        else:
            print("Please make a selecion of either 1, 2, or 3")
            return 1

        
def bmi():
    print("BMI")
    return 5

def retirement():
    print("Retirement")
    return 3