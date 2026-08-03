class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp, rp  = 0, 1
        char_set = set()
        length = 0 

        for rp in range(len(s)):
            while s[rp] in char_set:
                char_set.remove(s[lp])
                lp +=1
            char_set.add(s[rp])
            length = max(length, rp - lp +1)
        return length

        