class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arrmax = -1
            for j in range(i + 1, len(arr)):
                arrmax = max(arrmax, arr[j])
            arr[i] = arrmax
        return arr