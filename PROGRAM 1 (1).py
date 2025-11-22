'''
Create a python program that asks the user how far they want to travel. If they want to travel less than three miles tell them to ride Bicycle. 
if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-Cycle. 
if they want to travel three hundred miles or more tell them to drive Super-Car
'''
dist=int(input("ENTER THE DISTANCE IN MILES"))
if (dist<3):
    print(f"YOU BETTER TAKE BICYCLE FOR {dist} miles")
elif(dist>3 and dist<300):
    print(f"You beter take a motor cycle for {dist} MILES RIDE")
else:
    print(f"YOU BETER TAKE A CAR FOR {dist} MILES RIDE")