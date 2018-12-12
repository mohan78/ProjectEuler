"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#Sum square difference

sum1 = sum([i**2 for i in range(1,101)]) # List comprehension for sum of squares
sum2 = sum([i for i in range(1,101)])**2 # List comprehension for square of sum
print("Sum of squares for numbers upto 100 is ",sum1)
print("Square of sum for numbers upto 100 is ",sum2)
print("Differnce is ", sum2-sum1)
