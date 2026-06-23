from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            anagramGroups[key].append(word)
        
        return list(anagramGroups.values())

    
        



        