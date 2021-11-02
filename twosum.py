class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i


lst = [2,4,6,3,9]
tg = 6
cc = Solution()
twosm = cc.twoSum(lst,tg)
print(twosm)