# import math
# a=18
# b=18
# c=a+b
#
# print("The Solution is",c);
#
#
#
# 1. Write a program to print * or # pattern in python.
# #
# ##
# ###
# ####
# #####
#
#
# for a in range (1,6,2):
#     print("#" * a);
# #
#
#
# 2. Use REPL and print the table of 10 using it.
# for i in range(1,11):
#     print(f"10 x{i}={10*i}");
#
#3. Write a Python program to find the remainder when a number is divided by Z(Integer).
#

# 4.Use a comparison operator to find out whether a given variable a is greater than b or not.
# (Take a=34 and b=80)
#
# a=9
# b=10
#
# if a>b:
#     print(f"The greater value is a")
# else:
#     print(f"The grester value is b")

#Write a Python program to find the average of two numbers entered by the user.

# a= float(input("Enter any Number:"))
# b= float(input("Enter any Number:"))
#
#
# z=((a+b)/2)
#
# print("THe average value =",z)

# Write a Python program to calculate the square of a number entered by the user.

# a =float(input("To find a Square, Enter any Value:"))
# z=a*a
#
# print("The Required Square Value :",z)


# a=31
# print(type(a))


# a="SwapnilKihsorDixit"
# print(a.count("i"))
# print(len(a))

# 2.	Write a program to format the following letter using escape sequence characters.

# print("Dear  Candidate,\n\t We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us. \nThank you,\n HR")

# While Loop
# i=0
# while i<5:
#     print("Hello")
#     i=i+1
# else:
#     print("Task Complete")

# For Loop

# a=[1,2,3,4,6,5, "Swapnil"]
# for i in a:
#     print(i)

def is_product_of_consecutive_integers(s):
    # Check for all substrings of the string
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]

            # Convert the substring to an integer
            num = int(substring)

            # Ignore zero
            if num == 0:
                continue

            # Check if the number can be expressed as N * (N + 1)
            n = int((num ** 0.5))  # Estimate starting point for N
            if n * (n + 1) == num:
                return True

    return False


# Example usage
string = "1242"
print(is_product_of_consecutive_integers(string))  # Output: True

