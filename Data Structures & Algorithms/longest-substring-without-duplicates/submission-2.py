class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right = 0, 0 
        lswrc = 0
        duplicate = set()

        for right in range(len(s)): 
            while s[right] in duplicate:
                duplicate.remove(s[left])
                left +=1 
            duplicate.add(s[right])
            lswrc = max(lswrc, right - left + 1 )
        return lswrc