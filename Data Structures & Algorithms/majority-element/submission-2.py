class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = []
        for i in nums:
            if nums.count(i) > len(nums)//2:
                majority.append(i)
                return i
        