class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1 = []
        for i in nums:
            if i not in list1:
                list1.append(i)
        list1.sort(key=nums.count, reverse = True)
        return list1[:k]
    

s1 = Solution()
print(s1.topKFrequent([1,2,2,3,3,3],2))