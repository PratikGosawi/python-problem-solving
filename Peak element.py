class Solution:
    def peakElement(self ,arr):
        current_num = 1
        length_of_array = len(arr)

        if length_of_array == 1:
            return 0
        elif length_of_array > 1:
            while current_num < length_of_array:
                if current_num == (length_of_arra y -1) and (arr[current_num] > arr[current_num - 1]):
                    return current_num
                elif current_num == (length_of_arra y -1) and (arr[current_num] < arr[current_num - 1]):
                    return current_nu m -1

                elif (arr[current_num] > arr[current_num - 1]) and (arr[current_num] > arr[current_num + 1]):
                    return current_num

                current_num = current_num + 1
        else:
            return -1