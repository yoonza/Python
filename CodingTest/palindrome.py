def isPalindrome(x):
    if x == x[::-1]:
        return True

def solution(s):
    M = 0 
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if isPalindrome(s[i:j]):
                if M < len(s[i:j]):
                    M = len(s[i:j])
    return M
