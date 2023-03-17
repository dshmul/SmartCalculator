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
            val1 = inquirer.number(
                message=f"Enter {messages[operation][0]}:",
                float_allowed=True,
                validate=EmptyInputValidator()
            ).execute()

            val2 = inquirer.number(
                message=f"Enter {messages[operation][1]}:",
                float_allowed=True,
                validate=EmptyInputValidator()
            ).execute()

            val1 = float(val1)
            val2 = float(val2)

            if operation == "Addition":
                print(f"Result: {val1 + val2}")
            elif operation == "Subtraction":
                print(f"Result: {val1 - val2}") 
            elif operation == "Multiplication":
                print(f"Result: {val1 * val2}") 
            elif operation == "Division":
                print(f"Result: {val1 / val2}")
            elif operation == "Exponent": #TODO: fix error
                print(f"Result: {val1 ^ val2}")
            elif operation == "Root": #TODO: handle divide by 0
                print(f"Result: {val1 ^ (1/val2)}")
        
        # alternate operations
        elif operation == "Date Delta": #TODO: add data validator
            pass
        elif operation == "Univariate Equation":
            pass
        elif operation == "Quadratic Equation":
            pass

        print()

if __name__ == "__main__":
    main()