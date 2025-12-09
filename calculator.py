#!/usr/bin/env python3
# Simple calculator
def add(a, b):
"""Addition function"""
return a + b
def subtract(a, b):
"""Subtraction function"""
return a - b
def multiply(a, b ):
"""Multiplication function"""
return a * b
def main():
print("=== Simple Calculator ===")
print("1. Addiction")
print("2. Subtraction")
print("3. Multiplication")
choice = input("\nSelect operation (1, 2 or 3): ")
num1 = float(input("Enter first number: ")
num2 = float(input("Enter second number: ")
if choice == "1":
result = add(num1, num2)
print(f"\n{num1} + {num2} = {result}")
elif choice == "2":
result = subtract(num1, num2)
print (f"\n{num1} - {num2} = {result}")
elif choice == "3":
result = multiply(num1, num2)
print(f"\n{num1} * {num2} = {result}")
else:
print("Invalid choice!")
if __name__ == "__main__":
main()

if  __name__ == "__main__":
main()

