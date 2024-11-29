# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/502/
class Solution:
    # idea is to split by dot and compare each of it
    # in case of length is different, we stop at minimum length (break)
    # after it we continue iterate the longer one and check the value, if its bigger than 0, its the bigger one
    # its because we assume the shorter one to be 0
    # time complexity : O(n + m)
    # space complexity : O(1)
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        i = 0
        j = 0

        while True:
            if int(v1[i]) > int(v2[j]):
                return 1
            elif int(v1[i]) < int(v2[j]):
                return -1
            
            i += 1
            j += 1

            if i == len(v1):
                break

            if j == len(v2):
                break
        
        if i < len(v1):
            for ii in range(i, len(v1)):
                if int(v1[ii]) > 0:
                    return 1

        if j < len(v2):
            for ii in range(j, len(v2)):
                if int(v2[ii]) > 0:
                    return -1
            
        return 0
        pass

s = Solution()

version1 = "1.01"
version2 = "1.001"
result = s.compareVersion(version1, version2)
print(result)
assert result == 0

version1 = "1.2" 
version2 = "1.10"
result = s.compareVersion(version1, version2)
print(result)
assert result == -1

version1 = "1.0"
version2 = "1.0.0.0"
result = s.compareVersion(version1, version2)
print(result)
assert result == 0
