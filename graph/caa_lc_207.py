# vedio: https://www.youtube.com/watch?v=EgI5nU9etnU&t=371s
# For question understanding https://www.youtube.com/watch?v=kXy0ABd1vwo

from typing import List

class Solution():

    def canFinish(self,numCourses:int,prerequisites:List[List[int]])->bool:

        preMap = { i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)


        #visitSet = all courses along the curr DFS path

        visitSet=set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False

            visitSet.remove(crs)
            preMap[crs]=[]

            return True

        for crs in range(numCourses):
            if not dfs(crs):return False

        return True

# print(Solution().canFinish(2,[[1,0],[0,1]]))

print(Solution().canFinish(5,[[0,1],[0,2],[1,3],[1,4],[3,4]]))