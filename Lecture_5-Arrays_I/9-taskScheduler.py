"""
See explanation in the description
"""
def taskScheduler(arr, n):
    maximum=0
    maxCount=0
    freq={}
    for c in arr:
        freq[c] = freq.get(c,0) + 1 #Shortcut to check if key exists in dict
        if maximum < freq[c]:
            # Remember to do this in the 2 lines below or else maxCounter will be wrong
            # You need to reset maxCounter whenever there is a new winner. And hence also you cant do maximum++ here
            maximum = freq[c]
            maxCount=1
        elif maximum == freq[c]:
            maxCount += 1
    #Remaining logic below you just need to understand and remember
    #The goal of the below lines is to compute the idle slots
    partCount = maximum-1 #Since partitions are only between the most frequent
    partLength = n - maxCount -1 #Since you would have patterns like A B ? ? A B ? ? A B
    emptySlots = partCount * partLength #This is intuitive
    availableTasks = len(arr) - maximum*maxCount #These are the remaining tasks to be allocated to emptySlots
    idles = max(0, emptySlots-availableTasks) #Again intuitive
    return len(arr) + idles

print(taskScheduler(['A','A','B','B','A','B'],2))