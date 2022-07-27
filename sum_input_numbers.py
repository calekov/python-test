from datetime import datetime

print("\n--- start app at {} ---".format(datetime.now()))
print()

num1 = int(input("Insert first number: "))
num2 = int(input("Insert second number: "))

print()
print("Sum: {} + {} = {}".format(num1, num2, (num1 + num2)))
print("Subtraction: {} - {} = {}".format(num1, num2, (num1 - num2)))
print("Multiplication: {} * {} = {}".format(num1, num2, (num1 * num2)))
print("Divide: {} / {} = {}".format(num1, num2, (num1 / num2)))
print("Modulo: {} % {} = {}".format(num1, num2, (num1 % num2)))
print("Exponent: {} ** {} = {}".format(num1, num2, (num1 ** num2)))

print()
print("--- end at {} ---\n".format(datetime.now()))