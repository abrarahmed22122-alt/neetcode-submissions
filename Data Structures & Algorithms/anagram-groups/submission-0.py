class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            newKey = "".join(sorted(word))
            if newKey not in anagram_map:
                anagram_map[newKey] = []
            anagram_map[newKey].append(word)
        return list(anagram_map.values())
    
s1 = Solution()
print(s1.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
