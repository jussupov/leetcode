#1342. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num):
        cnt = 0
        while num:
            num = num // 2 if num % 2 == 0 else num - 1
            cnt += 1
        return cnt


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSteps(14))