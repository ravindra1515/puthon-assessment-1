'''4.A traffic system records the average speed of vehicles every hour for 12 hours.
Write a program that: Reads 12 speed values (floats). Calculates the average speed. Displays whether traffic flow was “Slow” (avg < 40), “Normal” (40–80), or “Fast” (avg > 80).
Concepts: list input, loop, conditional check, average calculation.'''
14
speeds = []
for i in range(12):
    while True:
        try:
            speed = float(input(f"Enter speed for hour {i+1}: "))
            speeds.append(speed)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for speed.")

average_speed = sum(speeds) / len(speeds)
if average_speed < 40:
    print("Traffic flow was Slow")
elif 40 <= average_speed <= 80:
    print("Traffic flow was Normal")
else:
    print("Traffic flow was Fast")
print(f"Average speed: {average_speed:.2f} km/h")
print("PROGRAM 4 COMPLETED")