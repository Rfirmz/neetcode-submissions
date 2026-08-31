from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        return_dict = defaultdict(list)

        for string in strs:

            count = [0] * 26
            for letter in string:
                count[ord(letter) - ord('a')] += 1
            
            return_dict[tuple(count)].append(string)
        
        return list(return_dict.values())