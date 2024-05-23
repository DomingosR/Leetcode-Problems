class Solution(object):
    def maxChunksToSorted(self, arr):
        currMax = -1
        numChunks = 0
        
        for i in range(len(arr)):
            currMax = max(currMax, arr[i])
            if currMax == i:
                numChunks += 1
                currMax = -1
            
        return numChunks