class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total = m + n
        
        if total%2 == 0:
            end = total/2
            flag = True
        else:
            end = (total+1)/2
            flag = False
            
        i = j = 0
        
        while (i<m or j<n) and end!=1:
            if i<m and j<n:
                if nums1[i]<nums2[j]:
                    i+=1
                else:
                    j+=1
            elif i<m:
                i+=1
            else:
                j+=1
            end-=1
        if not flag:
            if i<m and j<n:
                return nums1[i] if (nums1[i]<nums2[j]) else nums2[j]
            elif i<m:
                return nums1[i]
            else:
                return nums2[j]
        else:
            if i<m and j<n:
                if nums1[i] < nums2[j]:
                    if i+1 <m:
                        new = min(nums1[i+1], nums2[j])
                    else:
                        new = nums2[j]
                    return (nums1[i]+new)/2
                else:
                    if j+1 < n:
                        new = min(nums2[j+1],nums1[i])
                    else:
                        new = nums1[i]
                    return (nums2[j] + new)/2
            elif i<m:
                return (nums1[i]+nums1[i+1])/2
            else:
                return (nums2[j]+nums2[j+1])/2
                    
                
                
        
            
        