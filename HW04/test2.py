# Recursive implementation for minimum 
# cost convex polygon triangulation
from math import sqrt
MAX = 1000000.0
 
# A utility function to find distance
# between two points in a plane
def dist(p1, p2):
    return sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + \
                (p1[1] - p2[1])*(p1[1] - p2[1]))
 
# A utility function to find cost of 
# a triangle. The cost is considered
# as perimeter (sum of lengths of all edges)
# of the triangle
def cost(points, i, j, k):
    p1 = points[i]
    p2 = points[j]
    p3 = points[k]
    return dist(p1, p2) + dist(p2, p3) + dist(p3, p1)
 
 
# A recursive function to find minimum 
# cost of polygon triangulation
# The polygon is represented by points[i..j].
def mTC(points, i, j):
     
    # There must be at least three points between i and j
    # (including i and j)
    if (j < i + 2):
        return 0
         
    # Initialize result as infinite
    res = MAX
     
    # Find minimum triangulation by considering all
    for k in range(i + 1, j):
        res = min(res, (mTC(points, i, k) + \
                        mTC(points, k, j) + \
                        cost(points, i, k, j)))
     
    return round(res, 4)
 
 
# Driver code
points = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
n = len(points)
print(mTC(points, 0, n-1))