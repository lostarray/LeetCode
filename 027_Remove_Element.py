# Given an array and a value, remove all instances of that value in place and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example:
# Given input array nums = [3,2,2,3], val = 3
#
# Your function should return length = 2, with the first two elements of nums being 2.
#
# Hint:
#
# Try two pointers.
# Did you use the property of "the order of elements can be changed"?
# What happens when the elements to remove are rare?
#
# Tags: Array, Two Pointers


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0

        while i < length:
            while nums[i] == val and length > i:
                length -= 1
                nums[i] = nums[length]

            i += 1

        return length


if __name__ == '__main__':
    nums = [4, 5]
    print Solution().removeElement(nums, 5)
    print nums
