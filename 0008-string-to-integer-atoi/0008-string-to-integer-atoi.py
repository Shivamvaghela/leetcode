class Solution:
    def myAtoi(self, s):
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # 1️⃣ Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # If string is empty after removing spaces
        if i == n:
            return 0
        
        # 2️⃣ Check sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # 3️⃣ Convert digits
        result = 0
        
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # 4️⃣ Check overflow before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result