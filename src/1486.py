#1486. XOR Operation in an Array

class Solution:
    def xorOperation(self, n, start):
        arr = [start + 2*i for i in range(n)]
        x = arr[0]
        for i in range(1, len(arr)):
            x ^= arr[i]
        return x


if __name__ == "__main__":
    solution = Solution()
    print(solution.xorOperation(n = 5, start = 0))