#1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        limit = max(candies)
        return [candy + extraCandies >= limit for candy in candies]

if __name__ == "__main__":
    solution = Solution()
    print(solution.kidsWithCandies([12,1,12], 3))
        