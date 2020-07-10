#1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n):
        p, s = 1, 0
        while n > 0:
            t = n % 10
            n //= 10
            p *= t
            s += t
        return p - s
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.subtractProductAndSum(234))
        