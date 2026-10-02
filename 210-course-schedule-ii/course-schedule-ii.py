class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Courses with no prerequisites
        queue = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []
        index = 0

        # Topological sort
        while index < len(queue):
            course = queue[index]
            index += 1

            result.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Cycle exists
        if len(result) != numCourses:
            return []

        return result