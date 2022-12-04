#This will be need for work equation
#Simple project for student
import math
#Function to work equation
def motion():
    distance = int(input("Enter the distance (meter):"))
    time = int(input("Enter the time (second):"))
    velocity = distance/time
    print(f"Velocity is {velocity} meter per second")
def accleration():
    distance = int(input("Enter the distance (meter):"))
    time = int(input("Enter the time (second):"))
    initinal_velocity = int(input("Enter the initinal velocity:"))
    velocity = distance/time
    equation = (initinal_velocity - velocity)/time
    print(f"Accleration is {equation} meter per second square")
def average_velocity():
    velocity = int(input("Enter the velocity:"))
    initinal_velocity = int(input("Enter the initinal velocity:"))
    v_bar = (initinal_velocity + velocity)/2
    print(f"Average velocity is {v_bar}")
def force():
    m = int(input("Enter the mass of the body (in kg):"))
    a = int(input("Enter the acceleration:"))
    f = m*a
    print(f"Force of the body is:{f} Newton")
def free_fall():
    initinal_velocity = int(input("Enter the initinal velocity:"))
    gravity = 10 #Because the earth gravity is 10 meter per seconds
    time = int(input("Enter the time (second):"))
    equation = initinal_velocity+(gravity*time)
    print(f"The free fall velocity of the body is {equation} meter per second")
def pressuer():
    f = int(input("Enter the force:"))
    a = int(input("Enter the area of the object (in meter):"))
    p = f/a
    print(f"The pressure of the body of the is {p} pascal(unit is SI)")
#This is menu for the choice
print("1:Motion")
print("2:Acceleration")
print("3:Average velocity")
print("4:Force of the body by newton")
print("5:Free fall of the body")
print("6:Pressure")
#Your option will be excute the choose function
options = int(input("Choose an options:"))
if options == 1:
    motion()
elif options == 2:
    accleration()
elif options == 3:
    average_velocity()
elif options == 4:
    force()
elif options == 5:
    free_fall()
elif options == 6:
    pressuer()
#If your option is neither of above the program will exit
else:
    print("An error")
    exit()