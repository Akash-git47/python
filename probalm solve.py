# 5  Problem Solving
#Take a list of numbers from user input
#Print:
#Even numbers
#Odd numbers
#Largest and smallest number
#Bonus:
#Remove duplicates from the list
#Take a list of numbers from user input
numbers_input = input("Enter a list of numbers separated by spaces: ")
#Convert the input string into a list of integers
numbers = list(map(int, numbers_input.split()))
#Print even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)
#Print odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)
#Largest and smallest number
largest_number = max(numbers)
smallest_number = min(numbers)
print("Largest number:", largest_number)
print("Smallest number:", smallest_number)
#Bonus: Remove duplicates from the list
unique_numbers = list(set(numbers))
print("List with duplicates removed:", unique_numbers)
