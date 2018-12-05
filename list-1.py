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
