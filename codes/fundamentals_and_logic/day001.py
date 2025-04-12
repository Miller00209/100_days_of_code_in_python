print("Welcome to the calculator!")
print("Please enter a calculation (or type 'exit' to quit):")
while True:
    calc = input(">>> ")
    if calc.lower() == 'exit':
        print("Goodbye!")
        break
    try:
        result = eval(calc)
        print(f"The result is: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again.")