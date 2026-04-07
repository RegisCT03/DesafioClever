def isPalindrome(inputStr):
    if not inputStr: return False
    return inputStr == inputStr[::-1]