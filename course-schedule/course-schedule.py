from collections import defaultdict
from enum import Enum
class State(Enum):
    TO_VISIT = 0
    VISITING = 1
    VISITED = 2
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def build_graph():
            graph = defaultdict(list)
            for src, dest in prerequisites:
                graph[src].append(dest)
            return graph
        def dfs(start, states):
            # mark self as visiting
            states[start] = State.VISITING
            for next_vertex in graph[start]:
                # ignore visited nodes
                if states[next_vertex] == State.VISITED:
                    continue
                # revisiting a visiting node, CYCLE!
                if states[next_vertex] == State.VISITING:
                    return False
                # recursively visit neighbours
                # if a neighbour found a cycle, we return False right away
                if not dfs(next_vertex, states):
                    return False
            # mark self as visited
            states[start] = State.VISITED
            # if we have gotten this far, our neighbours haven't found any cycle, return True
            return True
        graph = build_graph()
        states = [State.TO_VISIT for _ in range(numCourses)]
        # dfs on each node
        for i in range(numCourses):
            if not dfs(i, states):
                return False
        return True
        
        
            
            
        
        
        