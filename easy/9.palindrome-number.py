#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        j = 0
        for i in range(len(a)):
            j -= 1
            if a[i] != a[j]:
                return False
            else: continue
        return True
        


# @lc code=end

