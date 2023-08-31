from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # build the anagram categories
        anagrams = defaultdict(list)
        for i in strs:
            sorted_string = ''.join(sorted(i))
            anagrams[sorted_string].append(i)
        # display the anagrams in an array
        return list(anagrams.values())
