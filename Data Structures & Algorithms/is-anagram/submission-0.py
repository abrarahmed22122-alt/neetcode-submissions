class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        list1 = list(t)
        for i in s:
            if i in list1:
                list1.remove(i)
            else:
                return False
        return True





checker = Solution()
print(checker.isAnagram("racecar","carrace"))
