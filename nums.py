#3. nums = [10, 5, 20, 8, 15]
#Perform:
#Find maximum value
#Find minimum value
#Find sum of elements
#Sort the list (ascending & descending)
#Find index of element 8
nums = [10, 5, 20, 8, 15]
#Find maximum value
max_value = max(nums)
print("Maximum value:", max_value)
#Find minimum value
min_value = min(nums)
print("Minimum value:", min_value)
#Find sum of elements
sum_of_elements = sum(nums)
print("Sum of elements:", sum_of_elements)
#Sort the list (ascending)
sorted_nums_asc = sorted(nums)
print("Sorted list (ascending):", sorted_nums_asc)
#Sort the list (descending)
sorted_nums_desc = sorted(nums, reverse=True)
print("Sorted list (descending):", sorted_nums_desc)
#Find index of element 8
index_of_8 = nums.index(8)
print("Index of element 8:", index_of_8)
