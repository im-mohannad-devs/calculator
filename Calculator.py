def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
def pow(a,b):
    return a**b

result = None

while True:
    print("========================================================================\n\t\t\tSimple Calculator\n========================================================================")
    print("Choose an operation:\n====================\n1-Add\t2-Subtract\t3-Multiplication\t4-Division\t5-Power\n========================================================================\n= : show result    C : clear    0-To stop\n========================================================================")
    choice = input("Enter operation:").upper()
    
    if choice not in ["1","2","3","4","5","=","C","0"]:
        print("Invalid choice!")
        continue
    
    if choice == "0":
        print("Done.")
        break
    
    if choice == "C":
        result = None
        print("The result has deleted")
        continue
    
    if choice == "=":
        if result is not None:
            print("Current result:",result)
        else:
            print("There is no result right now.")
        continue
    try:
        if result is None:
            result = float(input("Enter first number:"))
        
        else:
            print("Current result:", result)
            
        num = float(input("Enter next number:"))
            
        if choice == "1":
            result = add(result,num)
        
        elif choice =="2":
            result = sub(result,num)
    
        elif choice =="3":
            result = mul(result,num)
            
        elif choice =="4":
            result = div(result,num)
            
        elif choice =="5":
            result = pow(result,num)
        
        print("Updated result:",result)
        
    except ValueError:
        print("You can write numbers only")
    except ZeroDivisionError:
        print("You can't divide by zero")
