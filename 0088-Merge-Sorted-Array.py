class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index1 = m - 1
        index2 = n - 1
        currentIndex = m + n - 1

        while index1 >= 0 and index2 >= 0:
            if nums1[index1] >= nums2[index2]:
                nums1[currentIndex] = nums1[index1]
                index1 -= 1
            else:
                nums1[currentIndex] = nums2[index2]
                index2 -= 1
            currentIndex -= 1
        
        while index2 >= 0:
            nums1[currentIndex] = nums2[index2]
            index2 -=1
            currentIndex -= 1