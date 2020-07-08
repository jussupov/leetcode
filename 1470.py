#1470. Shuffle the Array

class Solution:
    def shuffle(self, nums, n):
        arr_1 = nums[:n]
        arr_2 = nums[n::]

        arr_res = []
        for i in range(n):
            arr_res.extend([arr_1[i], arr_2[i]])
        return arr_res

if __name__ == "__main__":
    solution = Solution()
    print(solution.shuffle([2,5,1,3,4,7], n=3))