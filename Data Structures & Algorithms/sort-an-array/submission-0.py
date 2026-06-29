class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        asc_list = []
        nums = nums.copy()  
        
        while nums:
            
            min_val = nums[0]
            for i in range(len(nums)):
                if nums[i] < min_val:  
                    min_val = nums[i]
            
            asc_list.append(min_val)   
            nums.remove(min_val)        
        
        return asc_list
            
                      
        