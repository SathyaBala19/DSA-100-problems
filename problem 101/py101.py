# LeetCode 14 = Longest Common Prefix
# Goal: given array ["flower","flow","flight"], answer is "fl".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # if the list is empty, there is no common prefix
        if not strs:
            return ""
        
        # take the first string as starting prefix
        prefix = strs[0]

        # compare prefix with every other string
        for word in strs[1:]:
            # keep reducing prefix until words starts with prefix
            while not word.startswith(prefix):
                # remove last character from prefix
                prefix = prefix[:-1]
                # if prefix becomes empty, no common prefix exists

                if prefix == "":
                    return ""
                
        return prefix
    
strs = ["flower", "flow", "flight"]

obj = Solution()
print(obj.longestCommonPrefix(strs))