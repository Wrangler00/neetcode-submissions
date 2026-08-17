class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(filter(str.isalnum,s))
        return text.casefold() == text[::-1].casefold()

        