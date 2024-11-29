class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        pass

s = Solution()

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
result = s.findItinerary(tickets)
print(result)
assert result == ["JFK","MUC","LHR","SFO","SJC"]
