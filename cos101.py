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
    print("What is the acceleration (in m/s2) ?:")
    acceleration = float(input())
    force = mass * acceleration
    print(f"The force is {force} Newtons.")

