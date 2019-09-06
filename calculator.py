from math import *

print("|\      /|      /\   ___________  |        |  ______")
print("| \    / |     /  \       |       |        | |       ")
print("|  \  /  |    /____\      |       |--------| |______ ")
print("|   \/   |   /      \     |       |        |       |")
print("|        |  /        \    |       |        |  _____|")
print("")

print("This Project was created by Kawojue Raheem\n ""\nFacebook: Kawojue Raheem CoderHacker\n """)

print("Whatsapp: +2349059137330\n ""\nGmail: kawojue08@gmail.com\n """)

print("IG: coderhacker_kawojue\n ""\n[1] Pythagorean Theorem Calculator\n "" \n[2] Basic Calculator\n """)

print("[3] Temperature Converter\n ""\n[4] Distance Calculator\n ""\n[5] Quadratic Calculator\n """)

print("[6] Area of Circle Calculator\n ""\n[7] Co-ordinate Calculator\n """)

try:
    opt = int(input("Enter your Operator: "))
    print("")

    if opt == 1:
        print("Pythagorean theorem")
        print("")
        print("     /|")
        print("    / |")
        print("hyp/  | opp")
        print("  /   |")
        print(" /____|")
        print("  adj  ")
        print("")

        print("[1] Pythagoras theorem calculator when you know the opp and adj\n """)

        print("[2] Pythagoras theorem calculator when you know the adj and hyp\n """)

        print("[3] Pythagoras theorem calculator when you know the hyp and opp\n """)

        calc = int(input("Enter your operator: "))
        print("")

        if calc == 1:
            adj = float(input("The Triangle Adjacent: "))
            print("")
            opp = float(input("The Triangle Opposite: "))
            hyp = sqrt((adj ** 2) + (opp ** 2))
            print("")
            print("The Pythagoras thorem of the Triangle is %.2f " % hyp)
    
        elif calc == 2:
            hyp = float(input("The Triangle Hypotenus: "))
            print("")
            opp = float(input("The Triangle Opposite: "))
            adj = sqrt((hyp ** 2) - (opp ** 2))
            print("")
            print("The Pythagoras thorem of the Triangle is %.2f " % adj)
    
        elif calc == 3:
            hyp = float(input("The Triangle Hypotenus: "))
            print("")
            adj = float(input("The Triangle Opposite: "))
            opp = sqrt((hyp ** 2) - (adj ** 2))
            print("")
            print("The Pythagoras thorem of the Triangle is %.2f " % opp)
    
        else:
            print("")
            print("Invalid Number or Operator")
    elif opt == 2:
        print("The operator must be multiplication, division, exponent, etc....\nThe valid operator are (*, /, ^, +, -).\n """)

        num1 = float(input("Enter the first number: "))
        print("")
        
        opr = str(input("Input an Operator: "))
        print("")
        
        num2 = float(input("Enter the second number: "))
        print("")

        if opr == "+":
            print(num1, "+", num2, "= %.2f" % (num1 + num2))
        elif opr == "-":
            print(num1, "-", num2, "= %.2f" % (num1 - num2))
        elif opr == "/":
            print(num1, "/", num2, "= %.2f" % (num1 / num2))
        elif opr == "*":
            print(num1, "X", num2, "= %.2f" % (num1 * num2))
        elif opr == "^":
            print(num1, "^", num2, "= %.2f" % (num1 ** num2))
        else:
            print("Invalid operator")

    elif opt == 3:
        print("[1] Changing of Degree Celcius to Degree Fahrenheit\n ""\n[2] Changing of Degree Farenheit to Degree Celcius\n """)

        num = int(input("Enter your operator: "))
        print("")

        if num == 1:
            C = float(input("The Degree in Celsius: "))
            F = ((C * (9/5)) + 32)
            print("")
            print("The Degree Fahrenheit is %.3f" % F)

        elif num == 2:
            f = float(input("The Degree Fahrenheit: "))
            c = (f - 32) / (1.8)
            print("")
            print("The Degree Celsius is %.3f" % c)

        else:
            print("")
            print("Invalid Input")
    elif opt == 4:
        print("Example; x(1, 4) assuming you are give this as the first part so the firstpart which is 1 will be the  one to")
        print("input first then follow by the second x part follow by the y(1, 3) first y part and the second of the y part.\n """)
        
        A = {}
        A[0] = float(input("The first x: "))
        A[1] = float(input("The second x: "))
        print("(", A[0], ",", A[1], ")")
        print("")

        B = {}
        B[0] = float(input("The first y: "))
        B[1] = float(input("The second y: "))
        print("(", B[0], ",", B[1], ")")
        print("")

        AB = sqrt((((B[0] - A[0]) ** 2) + (B[1] - A[1]) ** 2))
        print("")

        print("The Distance is %.3f" % AB)
    
    elif opt == 5:
        a = float(input("a = "))
        print("")
        
        b = float(input("b = "))
        print("")
        
        c = float(input("c = "))
        print("")
        
        d = b * b - 4 * a * c
        if d > 0:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            print("")
            print("x1 = %.3f; x2 = %.3f" % (x1, x2))
        elif d == 0:
            x1 = -b / (2 * a)
            print("")
            print("x1 = %.3f" % x1)
        else:
            print("")
            print("Complex Number")

    elif opt == 6:
        print("Area of a Circle\n """)

        print("[1] Area of a Circle when you know the Diameter\n ""\n[2] Area of a Circle when you know the Radius\n """)

        print("[3] Area of a Circle when you know the Circumference\n """)

        circ = int(input("Your Operator: "))
        print("")

        if circ == 1:
            d = float(input("Diameter: "))
            A = (pi/4) * (d**2)
            print("")
            print("A = %.3f" % A)
    
        elif circ == 2:
            r = float(input("Radius: "))
            A = pi * (r**2)
            print("")
            print("Area = %.3f" % A)

        elif circ == 3:
            C = float(input("Circumference: "))
            A = (C**2) / (4*pi)
            print("")
            print("Area = %.3f" % A)

        else:
            print("Invalid Number or Operator")
    
    elif opt == 7:
        print("Example; x(1, 4) assuming you are give this as the first part so the firstpart which is 1 will be the  one to")
        print("input first then follow by the second x part follow by the y(1, 3) first y part and the second of the y part. \n """)

        C = {}
        C[0] = float(input("The first x co-ordinate: "))
        C[1] = float(input("The second x co-ordinate: "))
        print("(", C[0], ",", C[1], ")")
        print("")

        D = {}
        D[0] = float(input("The first y co-ordinate: "))
        D[1] = float(input("The second y co-ordinate: "))
        print("(", D[0], ",", D[1], ")")
        print("")

        CC = (((C[0]) + (D[0])) / (2))

        DD = (((C[1]) + (D[1])) / (2))

        DC = (CC, DD)
        print("")

        print("The Co-ordinates are " + str(DC))
        
    else:
        print("")
        print("Invalid Input")
        
except:
    print("")
    print("Invalid Operator or Number")
