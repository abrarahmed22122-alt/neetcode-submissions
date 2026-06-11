class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, nums in enumerate(nums):
            difference = target - nums

            if difference in seen:
                return [seen[difference],i]

            seen[nums] = i
s1 = Solution()
print(s1.twoSum([3,4,5,6],7))
        