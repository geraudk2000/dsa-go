class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_freq = {}
        left = 0 
        most_repeating_char = 0 
        maxLenght = 0 

        for right in range(len(s)):
            right_char = s[right]
            char_freq[right_char] = char_freq.get(right_char, 0) + 1 
            most_repeating_char = max(most_repeating_char, char_freq[right_char])

            windows_size = right - left + 1 

            if windows_size - most_repeating_char > k : 
                left_char = s[left]
                char_freq[left_char] -= 1 
                left += 1 
            else: 
                maxLenght = max(maxLenght, windows_size)
        return maxLenght
