"""
You are given a list of segments, where each segment is represented by its left and right endpoints. 
The task is to find the minimum number of points needed to cover all the segments. 
If you can cover all the segments with points, return the points' positions; otherwise, return -1.

Implement the SegmentIntersection class with the following methods:

 --->  __init__(self, segments): The constructor that initializes the SegmentIntersection object with a list of segments.

 ---> find_min_points(self): A method that finds the minimum number of points needed to cover 
all the segments and returns both the count of points and their positions as a list.

Use the following implementation notes as a guide:

  ---> Sort the segments by their right endpoints.
  ---> Initialize an empty list called points to store the positions of points.
  ---> While there are segments left in the list:
  ---> Take the segment with the smallest right endpoint, x.
  ---> Add the right endpoint of x to the points list.
  ---> Remove any segments in the list that intersect with x.
  ---> Return the count of points and the list of points.
"""

class SegmentIntersection:
    def __init__(self, segments):
        self.segments = segments

    def find_min_points(self):
        # Sort segments by their right endpoints
        self.segments.sort(key=lambda x: x[1])
        
        points = []
        while self.segments:
            x = self.segments.pop(0)
            x1 = x[1]
            points.append(x1)
            # Remove segments that intersect with the current segment
            self.segments = [seg for seg in self.segments if seg[0] > x1]
        
        return len(points), points

if __name__ == "__main__":
    # Test cases
    n = int(input("Enter the number of segments: "))
    segments_list = []
    for _ in range(n):
        l, r = map(int, input("Enter left and right endpoints of a segment: ").split())
        segments_list.append((l, r))
    
    segment_intersection = SegmentIntersection(segments_list)
    min_points, points = segment_intersection.find_min_points()
    
    print("Minimum number of points needed:", min_points)
    print("Points:", points)


"""
Write the SegmentIntersection class and provide a sample test case to demonstrate its usage.

Sample Test Case:

# Initialize the segments
segments_list = [(1, 3), (2, 5), (5, 6), (7, 8)]

# Create a SegmentIntersection object
segment_intersection = SegmentIntersection(segments_list)

# Find the minimum number of points and their positions
min_points, points = segment_intersection.find_min_points()

# Output the result
print("Minimum number of points needed:", min_points)
print("Points:", points)

#Expected Outut
Minimum number of points needed: 2
Points: [3, 6]
"""
