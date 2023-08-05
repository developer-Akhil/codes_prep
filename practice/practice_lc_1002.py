from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        word = words[0]
        dict_val = {}

        for i in word:
            dict_val[i] = dict_val.get(i, 0) + 1        # bella {'b':1,'e':1,'l':2,'a':1}

        for word in words[1:]:

            for key in dict_val.keys():

                if key not in word:                     # b :  label

                    dict_val[key] = 0
                else:

                    dict_val[key] = max(dict_val[key],words.count(key))

        result = []
        # print(dict_val.items())
        for key,value in dict_val.items():

            result.extend([key]*value)

        return result





words = ["bella", "label", "roller"]

print(Solution().commonChars(words))
