# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums):
        x = []
        for i in range(len(nums)):
            x.append(sum(nums[:i+1]))
        return x

if __name__ == "__main__":
    solution = Solution()
    print(solution.runningSum([1, 2, 3, 4]))
