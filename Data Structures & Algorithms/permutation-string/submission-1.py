class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        target = [0] * 26

        for char in s1:
            target[ord(char) - ord('a')] += 1

        compare = [0] * 26

        start = 0
        end = len(s1) - 1
        for char in range(len(s1)):
            compare[ord(s2[char]) - ord('a')] += 1

        while end < len(s2) - 1:
            
            if compare == target:
                return True
            
            compare[ord(s2[start]) - ord('a')] -= 1
            start += 1

            end += 1
            compare[ord(s2[end]) - ord('a')] += 1

        if compare == target:
                return True 
    
        return False

            

            
        