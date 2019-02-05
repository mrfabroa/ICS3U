__author__ = 'eric'

"""
Write a program prompts for a number n and then finds the sum of all odd numbers 1 <= n.
"""

n = input("Enter a number: ")

total = 0
for i in range(1, n+1):
    total = total + i