#1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        N = len(nums)
        x = [0]*N
        for i in range(N):
            c = 0
            for j in range(N):
                if i != j and nums[i] > nums[j]:
                    c += 1
            x[i] = c
        return x
                              

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallerNumbersThanCurrent([8,1,2,2,3]))        