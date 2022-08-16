"""
https://www.geeksforgeeks.org/queue-based-approach-for-first-non-repeating-character-in-a-stream/


"""
# Python3 program to find Sum of all minimum and maximum
# elements Of Sub-array Size k.
from collections import deque

# Returns Sum of min and max element of all subarrays
# of size k
def SumOfKsubArray(arr, n , k):

    Sum = 0 # Initialize result

    # The queue will store indexes of useful elements
    # in every window
    # In deque 'G' we maintain decreasing order of
    # values from front to rear
    # In deque 'S' we maintain increasing order of
    # values from front to rear
    S = deque() #Monotonically increasing
    G = deque() #Monotonically decreasing


    # Process first window of size K

    for i in range(k):

        # Remove all previous greater elements
        # that are useless.
        while ( len(S) > 0 and arr[S[-1]] >= arr[i]):
            S.pop() # Remove from rear

        # Remove all previous smaller that are elements
        # are useless.
        while ( len(G) > 0 and arr[G[-1]] <= arr[i]):
            G.pop() # Remove from rear

        # Add current element at rear of both deque
        G.append(i)
        S.append(i)

    # Process rest of the Array elements
    for i in range(k, n):

        # Element at the front of the deque 'G' & 'S' is the largest and smallest element of previous window respectively
        Sum += arr[S[0]] + arr[G[0]]

        # Remove all elements which are out of this window
        while ( len(S) > 0 and S[0] <= i - k):
            S.popleft()
        while ( len(G) > 0 and G[0] <= i - k):
            G.popleft()

        # remove all previous greater element that are useless
        while ( len(S) > 0 and arr[S[-1]] >= arr[i]):
            S.pop() # Remove from rear

        # remove all previous smaller that are elements are useless
        while ( len(G) > 0 and arr[G[-1]] <= arr[i]):
            G.pop() # Remove from rear

        # Add current element at rear of both deque
        G.append(i)
        S.append(i)

    # Sum of minimum and maximum element of last window
    Sum += arr[S[0]] + arr[G[0]]

    return Sum

# Driver program to test above functions
arr=[2, 5, -1, 7, -3, -1, -2]
n = len(arr)
k = 3
print(SumOfKsubArray(arr, n, k))