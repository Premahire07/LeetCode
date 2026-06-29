class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""

        for ch in s:
            if ch.isalnum():  # Checks if char is letter or number othe than that get ignored
                text += ch.lower()

        return text == text[::-1] 
        