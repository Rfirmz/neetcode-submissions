class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        longest = 0
        track = dict()

        while r < len(s):

            # track indexes so
            # if new character found
            # continue to index after 
            # that repeated character

            if l == r:
                track[s[l]] = 0
                r += 1
                longest += 1
                continue
            
            if s[r] in track:
                l = max(track[s[r]] + 1, l)

            track[s[r]] = r
            
            
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest