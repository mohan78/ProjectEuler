# Sums of multiples of 3 and 5

num = int(input("Enter the limit number: "))
sum_of_3and5_multiples = 0
for i in range(1,num):
    if i % 3 == 0 or i % 5 == 0: #check whether the number is multiple of 3 or 5
        sum_of_3and5_multiples += i
print("The sum of 3 and 5 multiples below {} is {}".format(num,sum_of_3and5_multiples))
