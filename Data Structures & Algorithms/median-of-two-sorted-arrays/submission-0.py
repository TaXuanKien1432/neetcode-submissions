class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1 # we want to do binary search on smaller list to be faster
        while True:
            i = (left + right) // 2 # rightmost index of A's left portion
            j = half - (i + 1) - 1 # rightmost index of B's left portion

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft > Bright:
                right = i - 1
            elif Bleft > Aright:
                left = i + 1
            # Aleft + Bleft = overall left portion now
            else: 
                # even
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)



