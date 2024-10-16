"""Problem: Find the First Occurrence of a Number
Description: Given a list of integers, write a function 
that returns the index of the first occurrence of a
specified target number. If the target is not found, return -1.
Input Example: [3, 5, 7, 1, 4, 9], target = 4
Expected Output: 4"""


nums = [1, 4, 5, 6, 8]
target = 3
def first_occurance(nums: list[int], target: int) -> int:
    i: int = 0
    while i < len(nums):
        if nums[i] == target:
            return i
        i+=1 
    return -1
sol = first_occurance(nums=nums, target=target)
print(sol)



"""
Problem: Find the Maximum Element in a List
Description: Given a list of integers, 
write a function that finds and returns the maximum element in the list.
Input Example: [10, 22, 5, 75, 65, 80]
Expected Output: 80 
"""

nums_2 = [-5, -22, -1, 100]

def find_max(nums: list[int]) -> int:
    if not nums:
        return 404
    temp_max: int = nums[0]
    for i in nums:
        if temp_max < i:
            temp_max = i
    return temp_max


y = find_max(nums_2)
print(y)

"""
Problem: Find the First String that Meets a Condition
Description: Given a list of strings, 
write a function that finds the first string with a 
length greater than a specified value. Return the string,
or None if no string meets the condition.
Input Example: ["apple", "banana", "cherry", "date"], length = 5
Expected Output: "banana"
"""

words = ["apple", "banana", "cherry", "date"]
length = 5

def find_str_on_condition(words: list[str], length: int) -> str:
    if not words:
        return None
    for word in words:
        if len(word) > length:
            return word
    return None

z = find_str_on_condition(words=words, length=length)
print(z)
