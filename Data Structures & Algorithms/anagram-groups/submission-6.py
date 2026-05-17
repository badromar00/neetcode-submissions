class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list) # [1, 0, 1]: ["ac", "ca"]

        for word in strs:
            freq_arr = [0] * 26
            for char in word:
                freq_arr[ord(char) - ord('a')] += 1
            anagrams[tuple(freq_arr)].append(word)

        return [val for val in anagrams.values()]



        

        