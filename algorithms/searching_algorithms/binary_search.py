

"""
Problem: Search for a Target Number in a Sorted List
Description: Given a sorted list of integers,
write a function that returns the index of a target number.
If the target is not present, return -1.
Input Example: [1, 3, 5, 7, 9, 11], target = 7
Expected Output: 3
"""
from math import floor
nums = [1, 3, 5, 7, 9, 11]
target = 7

def get_target_2(nums, target):
    low = 0
    high = len(nums) - 1

    while low<=high:
        middle = floor((high+low)/2)
        if target > nums[middle]:
            low = middle + 1
        elif target < nums[middle]:
            high = middle -1 
        else:
            return middle





"""
Problem: Find the First Occurrence of a Target in 
a Sorted List with Duplicates
Description: Given a sorted list of 
integers (with possible duplicates), 
write a function that returns the index of 
the first occurrence of the target number. 
If the target is not found, return -1.
Input Example: [1, 2, 2, 2, 4, 5], target = 2
Expected Output: 1
"""

nums = [1, 2, 2, 2, 4, 5]
target = 2

def get_first_occurance(nums, target):

    low = 0
    high = len(nums) - 1

    while low<=high:
        mid = floor((low+high)/2)

        if nums[mid] == target:

            if mid == 0 or nums[mid-1] != target:
                return mid
            else:
                high = mid - 1
        
        elif nums[low] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


y  = get_first_occurance([1, 2, 2, 2, 4, 5], 2)
print(y)