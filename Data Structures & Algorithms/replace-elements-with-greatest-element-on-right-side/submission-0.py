class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arr[i] = 0
            for j in range(i, len(arr)):
                if arr[i] < arr[j]:
                    arr[i] = arr[j]
        
        arr[-1] = -1
        return arr