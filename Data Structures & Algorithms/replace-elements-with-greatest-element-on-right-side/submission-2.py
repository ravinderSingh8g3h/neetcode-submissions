class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1 : return [-1]
        mxele = -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] >= mxele :
                temp = arr[i]
                arr[i] = mxele
                mxele= temp
            else:
                arr[i] = mxele
        arr[-1] = -1
        return arr     