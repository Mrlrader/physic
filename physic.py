import math
def motion():
    distance = int(input("Enter the distance (meter):"))
    time = int(input("Enter the time (second):"))
    velocity = distance/time
    print(f"Velocity is {velocity}")
def accleration():
    distance = int(input("Enter the distance (meter):"))
    time = int(input("Enter the time (second):"))
    initinal_velocity = int(input("Enter the initinal velocity:"))
    velocity = distance/time
    equation = (initinal_velocity - velocity)/time
    print(f"Accleration is {equation}")
def average_velocity():
    velocity = int(input("Enter the velocity:"))
    initinal_velocity = int(input("Enter the initinal velocity:"))
    v_bar = (initinal_velocity + velocity)/2
    print(f"Average velocity is {v_bar}")