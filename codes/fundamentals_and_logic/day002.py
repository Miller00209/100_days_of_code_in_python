def f_to_c(f:int|float):
    return (f - 32) / 1.8
    

def c_to_f(c:int|float):
    return 1.8 * c + 32
    

print("Please enter the temperature type (or 'exit' to quit)")
while True:
    print("c - Celcius to Fahrenheit\nf - Fahrenheit to Celcius")
    tempt = input(">>> ")
    if tempt.lower() == "exit":
        exit(0)
    elif tempt.lower() == "c":
        temp = input("C° >>> ")
        try:
            f = c_to_f(eval(temp))
        except:
            print("error converting, please enter a valid temperature")
            continue
        else:
            print(f)
    elif tempt.lower() == "f":
        temp = input("F° >>> ")
        try:
            f = f_to_c(eval(temp))
        except:
            print("error converting, please enter a valid temperature")
            continue
        else:
            print(f)

