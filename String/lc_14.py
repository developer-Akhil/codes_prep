from typing import List


class Solution():

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:  # ["flower"]
            return strs[0]  # flower

        if len(strs) == 0:
            return ""

        prefix = strs[0]

        pref_len = len(prefix)  # 6

        for s in strs[1:]:  # s=flow | s=flight

            while prefix != s[0:pref_len]:  # flower != flight | flowe !=fligh | flow != flig | flo != fli | fl != fl
                prefix = prefix[0:(pref_len - 1)]  # prefix=flowe  | prefix=flow | prefix=flo | prefix=fl
                pref_len -= 1  # pref_len= 6-1=5  | pref_len=5-1=4 | pref_len=4-1=3 | pref_le=3-1=2

        if pref_len == 0:
            return ""
        return prefix


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))

