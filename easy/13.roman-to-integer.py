#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        library = {"I": 1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        liste = [library[x] for x in s if x in library]
        total = liste[-1]

        for x in range(1, len(liste)):
            if liste[x-1] >= liste[x]:
                    total += liste[x-1]
            else:
                total -= liste[x-1]
        return total

# @lc code=end

