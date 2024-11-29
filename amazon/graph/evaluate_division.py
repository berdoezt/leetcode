class DisjointSet:
    def __init__(self) -> None:
        self.root = {}
    
    def find(self, x):
        pass
    
    def union(self, x, y, val):
        
        pass
    

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        result = []

        ds = DisjointSet()
        n = len(equations)
        for i in range(n):
            equation = equations[i]
            value = values[i]

            ds.union(equation[0], equation[1], value)
        
        for query in queries:
            pass

        return result
        pass

s = Solution()

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
result = s.calcEquation(equations, values, queries)
print(result)
assert result == [6.00000,0.50000,-1.00000,1.00000,-1.00000]

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
result = s.calcEquation(equations, values, queries)
print(result)
assert result == [3.75000,0.40000,5.00000,0.20000]