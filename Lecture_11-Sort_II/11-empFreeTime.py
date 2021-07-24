"""
http://shibaili.blogspot.com/2019/02/759-employee-free-time.html

If you use Brute force to compute the free time, cost would be n^2 or even exponential. Instead use heaps to sort and
find non overlapping intervals
Approach:
1. Add start time of first interval of each employee to min heap
2. Iterate through min heap and pop left
3. If last_end (initialize to -1) is less than start then add start, last_end to result
4. set last_end to max(last_end, curr_end)
5. Push next interval for emp to heap and loop next
"""
import heapq

def employeeFreeTime(schedule):
    result = []
    min_heap = [(emp[0][0], eid, 0) for eid, emp in enumerate(schedule)]
    heapq.heapify(min_heap)
    last_end = -1
    while min_heap:
        t, eid, i = heapq.heappop(min_heap)
        if 0 <= last_end < t: #Note the trick of 0<=last_end since it has been initialized to 0 and you want
            #to prevent next line from executing in the first iteration
            result.append((last_end, t)) # Add to result if current_start is after last end
        last_end = max(last_end, schedule[eid][i][1])
        if i+1 < len(schedule[eid]): #push next interval for emp
            heapq.heappush(min_heap, (schedule[eid][i+1][0], eid, i+1))
    return result

print(employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]))