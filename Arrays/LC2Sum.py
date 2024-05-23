#Problem 01 - Easy


# O(n2) Solution

# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     final_array = []
#     n = 0
#     # print(nums)
#     length = len(nums)
#     print(length)
#     for i in range(0, length):
#         for j in range(i+1, length):
#             if nums[i]+nums[j] == target:
#                 final_array.append(i)
#                 final_array.append(j)
#                 print("yes")
#                 n = 1
#                 break
#             print(nums[i]+nums[j])

#         if n == 1:
#             break
#     print(final_array)



# O(n) Solution

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    pair_list = {}

    for i, num in enumerate(nums):
        if (target - num) in pair_list:
            return [i, pair_list[target - num]]
        pair_list[num] = i

nums = [-1,-2,-3,-4,-5]
target = -8
print(twoSum(nums, target))