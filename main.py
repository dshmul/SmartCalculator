from InquirerPy import inquirer 
from InquirerPy.validator import EmptyInputValidator
from datetime import datetime
import cmath
from sympy.solvers import solve
from sympy import Symbol

def main():
    messages = {"Addition": ["first value", "second value"],
                "Subtraction": ["first value", "second value"],
                "Multiplication": ["multiplicand", "multiplier"],
                "Division": ["dividend", "divisor"],
                "Exponent": ["base", "exponent"],
                "Root": ["base", "root"],
                "Date Delta": ["first date (DD/MM/YYYY)", "second date (DD/MM/YYYY)"],
                "Univariate Equation": ["univariate equation (use 'x' for variable)"],
                "Quadratic Equation": ["quadratic term (a)", "linear term (b)", "constant term (c)"],}

    while True:
        operation = inquirer.rawlist(
            message="Select Operation:",
            choices=[
                "Addition", 
                "Subtraction", 
                "Multiplication", 
                "Division", 
                "Exponent",
                "Root", 
                "Date Delta", 
                "Univariate Equation", 
                "Quadratic Equation", 
            ],
        ).execute()
        
        # operations with two vairables
        if operation not in ["Date Delta", "Univariate Equation", "Quadratic Equation"]: 
            val1 = float(inquire_number(messages[operation][0]))
            val2 = float(inquire_number(messages[operation][1]))

            try:
                if operation == "Addition":
                    print(f"Result: {val1 + val2}")
                elif operation == "Subtraction":
                    print(f"Result: {val1 - val2}") 
                elif operation == "Multiplication":
                    print(f"Result: {val1 * val2}") 
                elif operation == "Division":
                    print(f"Result: {val1 / val2}")
                elif operation == "Exponent": 
                    print(f"Result: {val1 ** val2}")
                elif operation == "Root": 
                    print(f"Result: {val1 ** (1/val2)}")
            except:
                print(f"Error: {messages[operation][1]} cannot be 0. Try again.\n")
                continue
        
        # alternate operations
        elif operation == "Date Delta": 
            date1_str = inquire_text(messages[operation][0])
            date2_str = inquire_text(messages[operation][1])

            # convert date string to date object
            try:
                date1 = datetime.strptime(date1_str, "%d/%m/%Y")
                date2 = datetime.strptime(date2_str, "%d/%m/%Y")
            except:
                print("Error: Invalid date provided.\n")
                continue
            
            # calculate difference in days
            delta = date2 - date1
            print(f"Result: {abs(delta.days)} days")

        elif operation == "Univariate Equation":
            input = inquire_text(messages[operation][0])

            left_side = input.split("=")[0].lstrip().rstrip()
            right_side = input.split("=")[1].lstrip().rstrip()
            
            x = Symbol('x')
            try:
                result = solve(f"{left_side} - ({right_side})" , x)
            except:
                print("Error: Invalid equation format provided. Include an '=' symbol in equation and put an '*' for multiplcation.\n")
                continue

            print(f"Result: {result}")

        elif operation == "Quadratic Equation": 
            a = float(inquire_number(messages[operation][0]))
            b = float(inquire_number(messages[operation][1]))
            c = float(inquire_number(messages[operation][2]))

            # calculate zeros
            try:
                result1 = (-b + cmath.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                result2 = (-b - cmath.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
            except: 
                print("Error: Invalid value provided for quadratic term.\n")
                continue

            print(f"Results: {result1}, {result2}")

        print()

def inquire_number(message):
    result = inquirer.number(
                message=f"Enter {message}:",
                float_allowed=True,
                replace_mode=True,
                validate=EmptyInputValidator()
            ).execute()
    return result

def inquire_text(message):
    result = inquirer.text(
                message=f"Enter {message}:",
            ).execute()
    return result
    
if __name__ == "__main__":
    main()