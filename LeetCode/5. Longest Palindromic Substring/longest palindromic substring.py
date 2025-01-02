def longestPalindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """
    if not s:  # Handle empty string case
        return ""

    longest = ""

    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Extract the palindrome

    for i in range(len(s)):
        # Odd length palindromes
        palindrome1 = expandAroundCenter(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1

        # Even length palindromes
        palindrome2 = expandAroundCenter(i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

# Example usage:
s1 = "babad"
print(longestPalindrome(s1))  # Output: "bab" or "aba"

s2 = "cbbd"
print(longestPalindrome(s2))  # Output: "bb"

s3 = "a"
print(longestPalindrome(s3)) # Output: "a"

s4 = "ac"
print(longestPalindrome(s4)) # Output: "a" or "c"

s5 = ""
print(longestPalindrome(s5)) # Output: ""