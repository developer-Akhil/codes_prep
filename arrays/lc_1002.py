import sys
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        db = {}
        result = []
        for char in A[0]:
            db[char] = db.get(char, 0) + 1

        for word in A[1:]:
            for key in db.keys():
                if key not in word:
                    db[key] = 0
                else:
                    db[key] = min(db[key], word.count(key))
        for key, value in db.items():
            result.extend([key] * value)
        return result


words = ["bella", "label", "roller"]
print(Solution().commonChars(words))

