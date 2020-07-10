#1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s):
        c = 0
        balance = 0
        for i in range(len(s)):
            if s[i] == 'R': balance += 1
            else: balance -= 1
            if balance == 0:
                c += 1
        return c


if __name__ == "__main__":
    solution = Solution()
    print(solution.balancedStringSplit("RLRRLLRLRL"))
        