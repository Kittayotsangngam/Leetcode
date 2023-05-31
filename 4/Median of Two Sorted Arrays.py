class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=len(nums1)+len(nums2)
        c=int((len(nums1)+len(nums2))/2)+1
        mdc=(len(nums1)+len(nums2))%2
        ans=[]
        idx1=0
        idx2=0
        for i in range(l):
            if idx1 <len(nums1) :
                if idx2<len(nums2) and (nums1[idx1]>nums2[idx2]) :
                    ans.append(nums2[idx2])
                    idx2+=1
                else:
                    ans.append(nums1[idx1])
                    idx1+=1
            elif idx2 <len(nums2):
                if idx1<len(nums1) and (nums2[idx2]>nums1[idx1]) :
                    ans.append(nums1[idx1])
                    idx1+=1
                else:
                    ans.append(nums2[idx2])
                    idx2+=1

        print(ans)
        if (mdc==1):
            return float(ans[c-1])
        else:
            return float((ans[c-1]+ans[c-2])/2)