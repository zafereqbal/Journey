class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Step 1: Build the adjacency list and in-degree array
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
            
        # Step 2: Initialize a queue with all courses that have no prerequisites (in-degree of 0)
        queue = [i for i in range(numCourses) if indegree[i] == 0]
        
        # Step 3: Process the queue using a pointer to avoid using standard library imports
        visited_count = 0
        head = 0
        
        while head < len(queue):
            current = queue[head]
            head += 1
            visited_count += 1
            
            # Reduce the in-degree of neighboring courses
            for neighbor in adj[current]:
                indegree[neighbor] -= 1
                # If a neighbor has no more prerequisites, add it to the queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If we successfully visited all courses, there are no cycles
        return visited_count == numCourses
