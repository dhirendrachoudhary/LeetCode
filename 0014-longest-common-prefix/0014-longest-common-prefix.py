class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for index in range(len(strs[0])):
            for string in strs[1:]:
                if index >= len(string) or string[index] != strs[0][index]:
                    return strs[0][:index]
        return strs[0]