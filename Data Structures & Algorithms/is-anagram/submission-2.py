class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        in_anagram: bool = False
        used_letters = []
        i = 0

        if len(str1) != len(str2):
            return False
        return sorted(str1) == sorted(str2)