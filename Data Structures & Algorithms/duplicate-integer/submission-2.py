class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # O(n log n) tim sort 
        result = False

        for i in range(1, len(nums)):   
            if nums[i-1] == nums[i]: #compare preceeing with current element 
                return True 
            
        return result

        '''
        Time => O(n log n) + O(n) = O(n log n)
        Space => O(n)
        '''