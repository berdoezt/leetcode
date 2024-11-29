import math

class Solution:
    def get_h(self, mid, piles):
        result = 0
        for i in piles:
            if i < mid:
                result += 1
            else:
                result += math.ceil(i / mid)
        
        return result
        pass

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min = 1
        max = None

        for i in piles:
            if max == None:
                max = i
                continue

            if i > max:
                max = i
        
        while min < max:
            mid = int((max - min) / 2) + min

            current_h = self.get_h(mid, piles)
            if current_h > h:
                min = mid + 1
            else:
                max = mid

                pass
        
        return min

        pass

s = Solution()

piles = [3,6,7,11]
h = 8
result = s.asdf(piles, h)
print(result)
assert result == 4

piles = [30,11,23,4,20]
h = 5
result = s.asdf(piles, h)
print(result)
assert result == 30

piles = [30,11,23,4,20]
h = 6
result = s.asdf(piles, h)
print(result)
assert result == 23