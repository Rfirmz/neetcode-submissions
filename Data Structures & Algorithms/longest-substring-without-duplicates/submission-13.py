class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mp = dict()
        l, r = 0, 0
        res = 0

        while r < len(s):

            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)

            mp[s[r]] = r
            res = max(res, r - l + 1)

            r += 1

        return res