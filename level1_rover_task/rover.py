import math


try:
    print("Enter origin coordinates:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    print("\nEnter destination coordinates:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))


    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx*dx + dy*dy)

    print("\nDistance to destination =", round(distance, 2), "m")

    
    print("\nEnter motion details:")
    u = float(input("Initial velocity: "))
    a = float(input("Acceleration: "))
    vmax = float(input("Top speed: "))

    if a <= 0:
        print("Acceleration should be positive")
    else:
        
        t1 = (vmax - u) / a
        if t1 < 0:
            t1 = 0

        
        s1 = u*t1 + 0.5*a*t1*t1

        if s1 >= distance:
            
            A = 0.5 * a
            B = u
            C = -distance

            t = (-B + math.sqrt(B*B - 4*A*C)) / (2*A)
        else:
            
            remaining = distance - s1
            t2 = remaining / vmax
            t = t1 + t2

        print("Time required =", round(t, 2), "seconds")

except:
    print("Invalid input! Please enter numbers only.")
