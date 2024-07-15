# Bubble Sort
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, 
# compares adjacent elements, and swaps them if they are in the wrong order.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("raw arr: ", arr, "\n")
sorted_arr = bubble_sort(arr)
print("Sorted array using bubble sort :", sorted_arr)


# Merge Sort
# Merge sort is a divide-and-conquer algorithm that divides the array into two halves, 
# sorts them, and then merges the sorted halves.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("Sorted array using merge sort: ", sorted_arr)
