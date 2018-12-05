"""
Given an array of ints, return True if 6 appears as either the first or last element in the array.
The array will be length 1 or more.
"""
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6


"""
Given an array of ints, return True if the array is length 1 or more,
and the first element and the last element are equal.
"""
def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]


"""
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
"""
def make_pi():
    return [3,1,4]


"""
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
Both arrays will be length 1 or more.
"""
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


"""
Given an array of ints length 3, return the sum of all the elements.
"""
def sum3(nums):
    return sum(nums)


"""
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
"""
def rotate_left3(nums):
   return [nums[1], nums[2], nums[0]]


"""
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
"""
def reverse3(nums):
    return [nums[2], nums[1], nums[0]]

"""
Given an array of ints length 3, figure out which is larger, the first or last element in the array,
and set all the other elements to be that value. Return the changed array.
"""
def max_end3(nums):
    max_num = max(nums[0], nums[2])
    new_list = list(map(lambda x: max_num, nums))

    return new_list

"""
Given an array of ints, return the sum of the first 2 elements in the array.
If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
"""
def sum2(nums):
    return sum(nums) if len(nums) < 3 else nums[0] + nums[1]
