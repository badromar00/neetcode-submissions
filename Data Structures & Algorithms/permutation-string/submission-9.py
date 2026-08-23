class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26
        window_length = len(s1)
        l = 0

        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1
        
        for r in range(len(s2)):
            if r - l + 1 > window_length:
                s2_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1

            s2_freq[ord(s2[r]) - ord('a')] += 1

            if s1_freq == s2_freq:
                return True


        return False



            
            

