# Largest 3 digit Palindrome number

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
first_num = 999
second_num = 999
palindrome = []

def isPalindrome(num):
  num = str(num)
  if num == num[::-1]:
    return True
  else:
    return False

for i in range(first_num,0,-1):
  for j in range(second_num,0,-1):
    num = i * j
    if isPalindrome(num):
      palindrome.append((num,i,j))

largest_palindrome = max([i for i in palindrome])
print("The Largest palidrome made by product of 3 digit numbers {} and {} is {}".format(largest_palindrome[1],largest_palindrome[2],largest_palindrome[0]))
