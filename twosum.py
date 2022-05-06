class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hasht = {}
        for i in range(len(nums)):
            if target - nums[i] in hasht:
                return [hasht[target - nums[i]], i]
            else:
                hasht[nums[i]] = i

lst = [2, 4, 6, 3, 9]
tg = 6
cc = Solution()
twosm = cc.twoSum(lst, tg)
print(twosm)


# USING enumerate FUNCTION
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         hasm = {}
#         for x,num in enumerate(nums):
#             if target-num in hasm:
#                 return [hasm[target-num],x]
#             elif target-num not in hasm:
#                 hasm[num] = x
# lst = [2, 4, 6, 3, 9]
# tg = 6
# cc = Solution()
# twosm = cc.twoSum(lst, tg)
# print(twosm)
