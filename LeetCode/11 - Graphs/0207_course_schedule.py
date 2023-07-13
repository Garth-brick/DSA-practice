from typing import List, Set


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    
    preMap = {i:[] for i in range(numCourses)}
    for course, prereq in prerequisites:
        preMap[course].append(prereq)

    def dfsCheck(course, visited: Set[int]):
        if course in visited:
            # if we have reached a course that we had already visited --> cycle exists
            return False

        if not preMap[course]:
            # if there are no prereqs for this course --> doable
            return True

        # if we still haven't visited this course then we need to check its prereqs
        # before checking prereqs, mark this course as visited
        visited.add(course)

        for prereq in preMap[course]:
            if not dfsCheck(prereq, visited):
                # if any of the prereqs are not possible --> not doable
                return False
            
        # setting this to an empty list so that this course immediately seen as doable later
        preMap[course] = []
        
        # removing this course from visited because it is doable and we don't want to trip up the dfsCheck algorithm later on
        visited.remove(course)
        return True


    for course in range(numCourses):
        if not dfsCheck(course, set()):
            return False
    return True

numCourses = 7
prereqs = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
print(canFinish(numCourses, prereqs))