import cmath

print("Welcome to the Quadratic Solver App.")
print("\nA quadratic equation is of the from ax^2 + bx + c = 0")
print("Your solutions can be real or complex.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

num_equations = int(input("How many equations would you like to solve today: "))

for num in range(num_equations):
    print("\nSolving equation #", num+1)
    print("--------------")
    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
    x1 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("\nThe solutions of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " are:")
    print("\n\tx1 =", x1)
    print("\tx2 =", x2)

print("\nThank you for using the Quadratic Solver App... Goodbye")


