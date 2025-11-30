class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)
        final_merged_string = ''
        for i in range(max(len_word1, len_word2)):
            if i < len_word1:
                final_merged_string += word1[i]     
            if i < len_word2:
                final_merged_string += word2[i]
        
        return final_merged_string