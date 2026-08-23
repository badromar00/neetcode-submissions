class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        most_freq = 0
        l = 0
        res = 0

        for r, char in enumerate(s):
            char_freq[char] += 1
            most_freq = max(most_freq, char_freq[char])

            while (r - l + 1) - most_freq > k:
                char_freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

"""
Input: 
char_freq = {X:1, Y:1 }
most_freq = 1
none_frequent_char_count = 0
res = 2

     l
      r
s = "AAABABB", k = 2

Output: 4

"""







"""
within a given window, keep track of most frequent char and its frequence
window will alwas be most frequent char + k
if window exceepd char + k -> move l
capture window length every iteration

"""
        