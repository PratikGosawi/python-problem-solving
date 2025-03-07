# Please change the array in-place
class Solution:
    def insertionSort(self, arr):
        for counter in range(len(arr) - 1):
            i = 0
            j = counter + 1
            while i < j:
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                i += 1


