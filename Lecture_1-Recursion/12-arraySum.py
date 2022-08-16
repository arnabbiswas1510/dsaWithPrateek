"""
Print all combinations of sums of 4 numbers in a 2D array below
This problem is to illustrate the working of exhaustive recursion - recursive calls within a loop
"""

def recur(arr, col, sum):
    if col > len(arr[0])-1:
        print(", sum ="+str(sum))
        return
    for row in range(len(arr)):
        #print(str(arr[row][col])+" + ", end="")#Uncomment to debug the flow
        #sum += arr[row][col] #This is a bug as sum will not change within stack
        recur(arr, col+1, sum+arr[row][col]) #Correct way to compute sum

arr=[[1,7,11,15],
      [2,5,9,13],
      [2,6,12,16],
      [4,8,10,14]]

recur(arr,0,0)