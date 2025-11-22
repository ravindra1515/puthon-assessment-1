'''3.You’re building a small program for a school. The user must enter the student’s name and marks in three subjects. The program should calculate the total, average, and display a grade. 
If marks are not between 0 and 100, show an error message. 
Concepts: Input/Output, data validation, arithmetic, if–elif–else.'''
name=input("ENTER THE STUDENT NAME:")
try:    
    mark1=float(input("ENTER THE MARKS OF SUBJECT 1:"))
    mark2=float(input("ENTER THE MARKS OF SUBJECT 2:"))
    mark3=float(input("ENTER THE MARKS OF SUBJECT 3:"))
    if(mark1<0 or mark1>100 or mark2<0 or mark2>100 or mark3<0 or mark3>100):
        print("ERROR: MARKS SHOULD BE BETWEEN 0 AND 100")
    else:
        total=mark1+mark2+mark3
        average=total/3
        print(f"TOTAL MARKS OF {name} IS: {total}")
        print(f"AVERAGE MARKS OF {name} IS: {average}")
        if(average>=90):
            grade='A'
        elif(average>=80):
            grade='B'
        elif(average>=70):
            grade='C'
        elif(average>=60):
            grade='D'
        else:
            grade='F'
        print(f"GRADE OF {name} IS: {grade}")
except ValueError:
    print("INVALID INPUT: PLEASE ENTER NUMERIC VALUES FOR MARKS")
finally:
    print("PROGRAM 3 COMPLETED")



