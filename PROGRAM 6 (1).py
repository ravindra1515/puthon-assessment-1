'''6.A company needs a program that reads employee names and their basic salary.
The program should: Calculate total salary including HRA (20%) and DA (10%).
Stop taking input when the user types "stop". Display each employee’s total salary at the end.
Concepts: while loop, arithmetic operations, condition check, formatted output.
'''
total_salary={}
while True:
    name=input("ENTER THE EMPLOYEE NAME:")  
    if name.lower() == "stop":
        break
    try:
        basic_salary=float(input(f"ENTER THE BASIC SALARY FOR {name}: "))
        if basic_salary < 0:
            print("ERROR: SALARY CANNOT BE NEGATIVE")
            continue
        hra = 0.20 * basic_salary
        da = 0.10 * basic_salary
        total = basic_salary + hra + da
        total_salary[name] = total
    except ValueError:
        print("INVALID INPUT: PLEASE ENTER A NUMERIC VALUE FOR SALARY")

for employee, salary in total_salary.items():
    print(f"TOTAL SALARY OF {employee} IS: {salary:.2f}")

print("PROGRAM 6 COMPLETED")