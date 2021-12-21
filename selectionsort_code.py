import time

def selection_sort(data, drawrectangle, delay):

    for i in range(1, len(data)):

        key = data[i]
        j = i- 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        drawrectangle(data, ['blue' if x == j or x == j + 1 else 'red' for x in range(len(data))])
        time.sleep(delay)
    drawrectangle(data, ['blue' for x in range(len(data))])
