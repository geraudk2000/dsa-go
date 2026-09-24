class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for idx, num in enumerate(nums): 

            diff = target - num 

            if diff in seen: 
                return [seen[diff], idx]
            
            seen[num] = idx 
        
        return [-1, -1]
        