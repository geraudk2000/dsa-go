class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        curSum = 0 
        left = -0
        res = float("inf")

        for right in range(len(nums)): 
            curSum += nums[right]
            while curSum >= target: 
                res = min(right - left + 1, res)
                curSum -= nums[left]
                left += 1
        return 0 if res == float("inf") else res