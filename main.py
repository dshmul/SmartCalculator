from InquirerPy import inquirer 
from InquirerPy.validator import EmptyInputValidator
from datetime import datetime
import math

def main():
    messages = {"Addition": ["first value", "second value"],
                "Subtraction": ["first value", "second value"],
                "Multiplication": ["multiplicand", "multiplier"],
                "Division": ["dividend", "divisor"],
                "Exponent": ["base", "exponent"],
                "Root": ["base", "root"],
                "Date Delta": ["first date (DD/MM/YYYY)", "second date (DD/MM/YYYY)"],
                "Univariate Equation": ["algebraic equation"],
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
            elif operation == "Root": #TODO: handle divide by 0
                print(f"Result: {val1 ** (1/val2)}")
        
        # alternate operations
        elif operation == "Date Delta": #TODO: add data validator
            date1_str = inquirer.text(
                message=f"Enter {messages[operation][0]}",
            ).execute()

            date2_str = inquirer.text(
                message=f"Enter {messages[operation][1]}",
            ).execute()

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
            pass
        
        elif operation == "Quadratic Equation": # TODO: fix logic
            a = float(inquire_number(messages[operation][0]))
            b = float(inquire_number(messages[operation][1]))
            c = float(inquire_number(messages[operation][2]))

            # calculate zeros
            result1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
            result2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

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

if __name__ == "__main__":
    main()