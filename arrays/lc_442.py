class Solution:

    def findDuplicates(self, nums):

        visited = set()
        result = []

        for i in nums:

            if i not in visited:

                visited.add(i)

            else:
                result.append(i)

        return result


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
