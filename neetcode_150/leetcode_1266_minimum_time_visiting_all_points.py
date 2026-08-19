class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(1,len(points)):
            horizontal = abs(points[i][0]-points[i-1][0])
            vertical = abs(points[i][1]-points[i-1][1])
            result = result + max(horizontal,vertical)
        return result 

        # cathc is the time rom one point to another is alsways max(h,v)
        