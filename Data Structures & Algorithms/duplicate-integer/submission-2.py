class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums
        
        empty_set = set() 
        
        for i in nums:
            if i in empty_set: 
                return True
            else:
                empty_set.add(i)
                
        return False

a = Solution()
print(a.hasDuplicate([1, 2, 3, 3]))  
print(a.hasDuplicate([1, 2, 3, 4]))  