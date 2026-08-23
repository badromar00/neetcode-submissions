class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0
        l = 0

        for r, char in enumerate(s):
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            maxLength = max(maxLength, r - l + 1)
        return maxLength

"""

Input: 
maxLenght = 3
seen = {, y, z}
       l
         r
s = "zxyzxyz"


"""