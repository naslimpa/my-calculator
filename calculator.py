#!/usr/bin/env python3
# Simple calculator
def add(a, b):
"""Addition function"""
return a + b
def main():
print("=== Simple Calculator ===")
num1 = float(input("Enter first number: ")
num2 = float(input("Enter second number: ")
result = add(num1, num2)
print(f"\n{num1} + {num2} = {result}")
if  __name__ == "__main__":
main()

