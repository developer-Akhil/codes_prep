from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = {}  # ={"aet":["eat","tea","ate"],"ant":["tan","nat"],"abt":["bat"]}
        for word in strs:

            sortedword = "".join(sorted(word))

            # sortedword = "".join(sorted("eat"))  = "aet" = "aet" = "ant" = "aet" = ant =abt

            if sortedword not in dict:
                dict[sortedword] = [word]

            else:
                dict[sortedword].append(word)  # = dict[aet] = tea

        result = []
        for item in dict.values():  # {["eat","tea","ate"],["tan","nat"],["bat"]}
            result.append(item)
        # result = [["eat","tea","ate"],["tan","nat"],["bat"]]
        return result


# Method 2


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
