"""
Counting sort works by iterating through the input, counting the number of times each item occurs, and using those
counts to compute an item's index in the final, sorted array.

Strengths:
Linear time. Counting sort runs in O(n)O(n) time, making it asymptotically faster than comparison-based sorting
algorithms like quicksort or merge sort.
Weaknesses:
Restricted inputs. Counting sort only works when the range of potential items in the input is known ahead of time.
Space cost. If the range of potential values is big, then counting sort requires a lot of space (perhaps more than O(n)

Algorithm:
1. First create a count array with the count of all elements in input array
2. This and next step enables you to generate an output array from a count array.Create a prefix sum array of count array
3. Create output array with count array showing index of input array element. Decrement count arr in each iteration
"""
def countSort(arr):

    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(26)]

    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[ord(i)-ord('a')] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(26):
        count[i] += count[i-1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])-ord('a')]-1] = arr[i]
        count[ord(arr[i])-ord('a')] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

# Driver program to test above function
arr = "geeksforgeeks"
ans = countSort(arr)
print("Sorted character array is % s" %("".join(ans)))