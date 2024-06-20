def selection_sort(array, steps):
    n = len(array)
    for i in range(steps):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        print(f"{i+1}. adım: {array}")

array = [7, 3, 5, 8, 2, 9, 4, 15, 6]
selection_sort(array, 4)