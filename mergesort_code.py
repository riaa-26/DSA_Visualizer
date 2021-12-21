import time

def merge_sort(data,l,m,r, drawrectangle, delay):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = data[l + i]

    for j in range(0, n2):
        R[j] = data[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
        k += 1


    while i < n1:
        data[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        data[k] = R[j]
        j += 1
        k += 1



def mergeSort(data, l, r):
    if l < r:

        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(data, l, m)
        mergeSort(data, m + 1, r)
        merge_sort(data, l, m, r)
        drawrectangle(data, ['blue' if x == j or x == i or x == k else 'red' for x in range(len(data))])
        time.sleep(delay)

    drawrectangle(data, ['blue' for x in range(len(data))])
