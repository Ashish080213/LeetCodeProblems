#Problem 26 - Easy

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 0
#         length = len(nums)
#         total = 1
#         while i < length-1:
#             if nums[i] == nums[i+1]:
#                 del nums[i+1]
#             else:
#                 i += 1
#                 total += 1
#             length = len(nums)
#         return total
    


# Optimal Solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        change = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[change] = nums[i]
                change += 1
        return change