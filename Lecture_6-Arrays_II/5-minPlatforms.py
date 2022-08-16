"""
Minimum Number of Platforms Required for a Railway/Bus Station
Difficulty Level : Medium
Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays that represent the arrival and departure times of trains that stop.

Examples:

Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
Explanation: There are at-most three trains at a time (time between 11:00 to 11:20)

Input: arr[] = {9:00, 9:40}
dep[] = {9:10, 12:00}
Output: 1
Explanation: Only one platform is needed.
"""

"""
Brute force method to keep running count of simultaneous platforms
"""

def minPlatformsSlow(arr, dep):
    maxPlatforms=0
    for i in range(len(arr)):
        platforms=1 #Since we iterate form the next index for j
        for j in range(i+1, len(dep)):
            if arr[i] >= arr[j] and arr[i] <= dep[j] \
                or arr[j] >= arr[i] and arr[j] <= dep[i]: #See keep Image
                platforms+=1
        maxPlatforms=max(maxPlatforms, platforms) #This works because of line 27 where platforms is reset for each index
    return maxPlatforms

arr=[910, 1200,1225,1238,1241, 1242,1243]
dep=[1100, 1230,1235,1330,1345,1346,1347]


"""
2 pointer approach that is faster after you sort both arrays
The key insight in both approaches is to count how many trains arrive before the "max platforms" one departs
"""
def minPlatforms(arr,dep):
    arr.sort()
    dep.sort()
    maxPlatforms=1
    platforms=1
    i=1 #Note that you start i with 1 and j with 0 since you start with first train which will always have a platform
    j=0
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            platforms+=1
            i+=1
        elif arr[i] > dep[j]:
            platforms-=1
            j+=1
        maxPlatforms=max(platforms, maxPlatforms)
    return maxPlatforms

print(minPlatforms(arr,dep))