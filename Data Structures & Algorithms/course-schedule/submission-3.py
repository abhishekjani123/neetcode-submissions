class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Declare the hash map
        premap = { i: [] for i in range(numCourses)}
        # Add all the courses and prereq in the Hashmap
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        # define visit as set() and def dfs(crs)
        visit = set()
        def dfs(crs):
            # two condition to be check is crs in visit set then return False 
            if crs in visit:
                return False # we found the cycle
            # Second condition if premap[crs] == [] return True
            if premap[crs] == []:
                return True
            # add crs in visit set
            visit.add(crs)

            # now for loop for prereq for that crs (pre in premap[crs])
            for pre in premap[crs]:
                # if dfs(pre) is not there then False
                if not dfs(pre):
                    return False
            # if there first remove the crs from the visit and make premap[crs] = []
            visit.remove(crs)
            premap[crs] = []
            # return True
            return True

        # Outside of dfs function, run for loop till numCourses
        for c in range(numCourses):
            #do call dfs(crs) if not return none
            if not dfs(c):
                return False
        #else return True
        return True
