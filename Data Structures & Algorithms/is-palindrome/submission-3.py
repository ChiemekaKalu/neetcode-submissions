class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnumS = ""
        for char in s:
            if char.isalnum():
                alnumS += char.lower()

        
        i = 0
        j = len(alnumS) - 1

        while j > i:
            if alnumS[i] == alnumS[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


        