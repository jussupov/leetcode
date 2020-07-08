#1108. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")


if __name__ == "__main__":
    solution = Solution()
    print(solution.defangIPaddr("1.1.1.1"))
