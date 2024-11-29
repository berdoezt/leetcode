'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
'''

class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1] * len(ratings)
        
        for i in range(len(ratings)):
            next = i + 1
            if next < len(ratings):
                if ratings[i] > ratings[next]:
                    if candies[i] <= candies[next]:
                        candies[i] = candies[next] + 1
            
            previous = i - 1
            if previous < 0:
                continue

            if ratings[i] > ratings[previous]:
                if candies[i] <= candies[previous]:
                    candies[i] = candies[previous] + 1

        for i in range(len(ratings) - 1, -1, -1):
            next = i + 1
            if next < len(ratings):
                if ratings[i] > ratings[next]:
                    if candies[i] <= candies[next]:
                        candies[i] = candies[next] + 1

            
            previous = i - 1
            if previous < 0:
                continue

            if ratings[i] > ratings[previous]:
                if candies[i] <= candies[previous]:
                    candies[i] = candies[previous] + 1

        result = 0
        for i in candies:
            result += i

        return result

s = Solution()

ratings = [3,2,1]
result = s.candy(ratings)
assert result == 6

ratings = [1, 2, 3]
result = s.candy(ratings)
assert result == 6

ratings = [1,0,2]
result = s.candy(ratings)
assert result == 5

ratings = [1,2,2]
result = s.candy(ratings)
assert result == 4

ratings = [1,2,87,87,87,2,1]
result = s.candy(ratings)
assert result == 13