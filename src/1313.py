#1313. Decompress Run-Length Encoded List

class Solution:
    def decompressRLElist(self, nums):
        arr = [[nums[i], nums[i+1]] for i in range(0, len(nums), 2)]
        x = []
        for el in arr:
            x += [el[1]]*el[0]
        return x


if __name__ == "__main__":
    solution = Solution()
    print(solution.decompressRLElist([1,2,3,4]))
        