# User function Template for python3

class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = temp


