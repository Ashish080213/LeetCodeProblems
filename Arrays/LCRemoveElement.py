# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         change = 0
#         length = len(nums)
#         i = 0
#         while i < length:
#             if nums[i] == val:
#                 nums.pop(i)
#             else:
#                 i += 1
#                 change += 1
#             length = len(nums)


# Optimal Solution but didnot get optimised output.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        change = 0
        for i in nums:
            if i != val:
                nums[change] = i
                change += 1
        return change
                
            