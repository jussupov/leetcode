#1389. Create Target Array in the Given Order

class Solution:
    def createTargetArray(self, nums, index):
        target_array = []
        for i in range(len(nums)):
            target_array.insert(index[i], nums[i])
        return target_array


if __name__ == "__main__":
    solution = Solution()
    print(solution.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))