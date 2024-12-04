print("This is a program created for Physics calculations.")
print("A: Force")
print("B: Work Done")
print("C: Speed")
print("D: Power")
print("E: Voltage")
# Ask for user input
inputMsg = input("Choose a physics operation between A-E:\n").lower()
# A function to calculate force
def a():
    mass = float(input("What is the mass (in kg)?:\n"))
    acceleration = float(input())
    force = mass * acceleration
    print(f"The force is {force} Newtons.")
# A function to calculate work done
def b():
    force = float(input("What is the force (in Newtons)?:\n"))
    distance = float(input("What is the distance (in metres)?:\n"))
    workDone = force * distance
    print(f"The workdone is {workDone} Joules.")
# A function to calculate speed
def c():
    distance = float(input("What is the distance (in metres)?:\n"))
    timeTaken = float(input("What is the time taken (in seconds)?:\n"))
    speed = distance / timeTaken
    print(f"The speed is {speed} m/s.")
# A function to calculate Power
def d():
    workDone = float(input("What is the workdone (in Joules)?:"))
    timeTaken = float(input("What is the time taken (in seconds)?:"))
    power = workDone / timeTaken
    print(f"The workdone is {power} J/s.")
