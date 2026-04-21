result =  float(input("Enter the first Number or 'q' to stop:"))

while True:
    operation = input("Which operation you want or press'q'to stop?\n(/ * - + ^):")
    if operation == "q":
        print("App is done.")
        print(result)
        break
    if operation not in ["+", "-", "*", "/", "^"]:
        print("Operation error")
        continue
    
    num = float(input("Enter the 2nd number:"))
    
    if operation == "/" and num ==0:
        print("You cannot divide by zero")
        continue
    if operation == "+":
        result += num
    elif operation == "-":
        result -= num
    elif operation == "*":
        result *= num
    elif operation == "/":
        result /= num
    elif operation == "^":
        result = pow(result,num)
        
    print(f"Result:{result}")