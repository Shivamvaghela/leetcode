class Solution:
    def longestPalindrome(self, s):
        
        if len(s) < 2:
            return s
        
        start = 0
        max_length = 1
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            
            len1 = expand(i, i)      # odd length
            len2 = expand(i, i + 1)  # even length
            
            curr_max = max(len1, len2)
            
            if curr_max > max_length:
                max_length = curr_max
                start = i - (curr_max - 1) // 2
        
        return s[start:start + max_length]