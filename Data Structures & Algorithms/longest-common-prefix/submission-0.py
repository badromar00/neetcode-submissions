class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        lgst_common = ""
        
        if not strs:
            return lgst_common
        
        for i in range(min_len):
            first_word_char_index = strs[0][i]
            for word in strs:
                if word[i] != first_word_char_index:
                    return lgst_common
            lgst_common += first_word_char_index
        return lgst_common


                

        