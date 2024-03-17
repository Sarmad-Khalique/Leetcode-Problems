from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: Dict[str, List[str]] = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]
            else:
                anagrams[sorted_s].append(s)
        return list(anagrams.values())

if __name__ == "__main__":
    inp = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(inp)) # [["eat","tea","ate"],["tan","nat"],["bat"]]