# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        		Aryan Dharangaonkar
# Section:      		561
# Assignment:           7.28 LAB: Kaprekar's constant
# Date:         		26 September 2023

# Input number
x = int(input("Enter a four-digit integer: "))
number = x
count = 0

while number != 6174 and number != 0:
    number = f"{number:0>4}"

    n1 = "".join(sorted(number))
    n2 = "".join(reversed(n1))
    
    n = int(n2) - int(n1)
    
    # Print without leading zeros
    print(int(number), "> ", end='')
    
    number = n
    count += 1
    
# Print the final result without leading zeros
if number == 6174:
    print(6174)
    print(x, "reaches", 6174, "via Kaprekar's routine in", count, "iterations")
