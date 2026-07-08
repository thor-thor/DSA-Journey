def isPalindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return isPalindrome(s,left+1,right-1)
s="RAJESH"
print(isPalindrome(s,0,len(s)-1))