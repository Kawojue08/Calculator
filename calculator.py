from math import *

info = '''
    |\      /|      /\   ===========  |        | |======
    | \    / |     /  \       |       |        | |       
    |  \  /  |    /====\      |       |========| |=====|
    |   \/   |   /      \     |       |        |       |
    |        |  /        \    |       |        |  =====|

    =====================================================
   | Created by Kawojue Raheem Olumuyiwa                 |
   | Facebook: Kawojue Raheem Olumuyiwa (CoderHacker)    |
   | Whatsapp: +2349059137330                            |
   | Gmail: kawojue08@gmail.com                          |
   | IG: coderhacker_kawojue                             |
    ===================================================
    '''
print(info)

while True:
    try:
        topic = ''' 
                OPERATORS
    [1] Pythagorean Theorem Calculator
    [2] Basic Calculator
    [3] Temperature Converter
    [4] Distance Calculator
    [5] Quadratic Calculator
    [6] Area of Circle Calculator
    [7] Co-ordinate Calculator
    [8] Average (Mean) Calculator
    [9] Multiplication Table Generator
    [10] Factorial Calculator
    [11] Fibonacci Generator
    [0] Exit
        '''
        print(topic)
        distance = '''Example; x(1, 4) assuming you are given this as the first part so the first part 
        which is 1 will be the one to input first then follow by the second x part, follow by the y(1, 3) first y part
        and then second of the y part. '''

        op = float(input("Enter your Operator: "))
        opt = round(op)
        print("")

        if opt == 1:

            tri = '''
    Pythagorean theorem
    
           /|
          / |
      hyp/  | opp
        /   |
       /____|
        adj
            '''
            print(tri)

            j = """
    [1] Pythagoras theorem calculator when you know the opp and adj
    [2] Pythagoras theorem calculator when you know the adj and hyp
    [3] Pythagoras theorem calculator when you know the hyp and opp
"""
            print(j)
            pytri = int(input("Enter your operator: "))
            print("")

            if pytri == 1:
                adj = float(input("The Triangle Adjacent: "))
                print("")
                opp = float(input("The Triangle Opposite: "))
                hyp = ((adj ** 2) + (opp ** 2)) ** (1 / 2)
                print("")
                print("The Pythagoras theorem of the Triangle is %.3f " % hyp)

            elif pytri == 2:
                pyh = float(input("The Triangle Hypotenuse: "))
                print("")
                ppo = float(input("The Triangle Opposite: "))
                ajd = ((pyh ** 2) - (ppo ** 2)) ** (1 / 2)
                print("")
                print("The Pythagoras theorem of the Triangle is %.3f " % ajd)

            elif pytri == 3:
                phy = float(input("The Triangle Hypotenuse: "))
                print("")
                jad = float(input("The Triangle Opposite: "))
                pop = ((phy ** 2) - (jad ** 2)) ** (1 / 2)
                print("")
                print("The Pythagoras theorem of the Triangle is %.3f " % pop)

            else:
                print("Invalid Number or Operator")

        elif opt == 2:
            print(
                "The operator must be multiplication, division, exponent, etc....\nThe valid operators are "
                "(*, /, ^, +, -).\n """)

            num1 = float(input("Enter the first number: "))
            print("")

            opr = str(input("Input an Operator: "))
            print("")

            num2 = float(input("Enter the second number: "))
            print("")

            if opr == "+":
                print(num1, "+", num2, "=", (num1 + num2))
            elif opr == "-":
                print(num1, "-", num2, "=", (num1 - num2))
            elif opr == "/":
                print(num1, "/", num2, "= %.5f" % (num1 / num2))
            elif opr == "*":
                print(num1, "x", num2, "= " + str(num1 * num2))
            elif opr == "^":
                print(num1, "^", num2, "= %.5f" % (num1 ** num2))
            else:
                print("Invalid operator")

        elif opt == 3:
            print(
                "[1] Changing of Degree Celsius to Degree Fahrenheit\n ""\n[2]"
                " Changing of Degree Fahrenheit to Degree Celsius\n """)

            num = int(input("Enter your operator: "))
            print("")

            if num == 1:
                C = float(input("The Degree in Celsius: "))
                F = ((C * (9 / 5)) + 32)
                print("")
                print("The Degree Fahrenheit is %.3f" % F)

            elif num == 2:
                f = float(input("The Degree Fahrenheit: "))
                c = (f - 32) / 1.8
                print("")
                print("The Degree Celsius is %.3f" % c)

            else:
                print("")
                print("Invalid Input")
        elif opt == 4:
            print(distance)

            A = dict()
            A[0] = float(input("The first x: "))
            A[1] = float(input("The second x: "))
            print("(" + str(A[0]) + ",", str(A[1]) + ")\n """)

            B = dict()
            B[0] = float(input("The first y: "))
            B[1] = float(input("The second y: "))
            print("(" + str(B[0]) + ",", str(B[1]) + ")\n """)

            AB = sqrt((((B[0] - A[0]) ** 2) + (B[1] - A[1]) ** 2))
            print("")

            print("The Distance is %.3f" % AB)

        elif opt == 5:
            print("Quadratic")
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))

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
            cir = '''Area of a Circle
    
    [1] Area of a Circle when you know the Diameter
    [2] Area of a Circle when you know the Radius
    [3] Area of a Circle when you know the Circumference 
            '''
            print(cir)

            circ = int(input("Your Operator: "))
            print("")

            if circ == 1:
                d = float(input("Diameter: "))
                A = (pi / 4) * (d ** 2)
                print("")
                print("Area = %.3f" % A)

            elif circ == 2:
                r = float(input("Radius: "))
                A = pi * (r ** 2)
                print("")
                print("Area = %.3f" % A)

            elif circ == 3:
                C = float(input("Circumference: "))
                A = (C ** 2) / (4 * pi)
                print("")
                print("Area = %.3f" % A)

            else:
                print("Invalid Number or Operator")

        elif opt == 7:
            print(distance)

            C = dict()
            C[0] = float(input("The first x co-ordinate: "))
            C[1] = float(input("The second x co-ordinate: "))
            print("(" + str(C[0]) + ",", str(C[1]) + ")\n """)

            D = dict()
            D[0] = float(input("The first y co-ordinate: "))
            D[1] = float(input("The second y co-ordinate: "))
            print("(" + str(D[0]) + ",", str(D[1]) + ")\n """)

            CC = (((C[0]) + (D[0])) / 2)
            DD = (((C[1]) + (D[1])) / 2)
            DC = (CC, DD)
            print("")

            print("The Co-ordinates are " + str(DC))

        elif opt == 8:
            print("Average Calculator")
            print("")
            num = int(input("Limit: "))
            print("")
            count = 0
            num1 = []

            for i in range(1, num + 1):
                number = float(input("Number: "))
                num1.append(number)
            for j in num1:
                count += j
            k = len(num1)
            avg = count / k
            print("")
            print("Average = %4f" % avg)

        elif opt == 9:
            print("         Multiplication Table Generator          ")
            print("")
            j = int(input("Limit: "))
            n = float(input("Number: "))
            print("")
            for gen in range(1, j + 1):
                print("|", n, "x", gen, "=", gen * n)

        elif opt == 10:
            print("        FACTORIAL            ")
            fac = int(input("Number: "))
            num = 1
            for i in range(1, fac + 1):
                num *= i
            print(str(fac) + "!", "=", num)

        elif opt == 11:
            print("           Fibonacci Generator          ")
            fib = int(input("Fibonacci: "))
            x, y = 0, 1
            for q in range(fib):
                x, y = y, x + y
            print("")
            print("The " + str(fib) + " Fibonacci number is " + str(x))

        elif opt == 0:
            print("Thanks for using my Script")
            exit()
        else:
            print("Invalid Input")
    except ValueError:
        print("The value you entered was incorrect (Error)")
    except TypeError:
        print("Complex Number")
    except ZeroDivisionError:
        print("Undefined")
    except OverflowError:
        print("Result too Large")
