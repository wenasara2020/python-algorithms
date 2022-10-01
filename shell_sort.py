# Shell sort in python

def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals

    interval = n // 2

    while interval > 0:

        for i in range(interval, n):

            temp = array[i]

            j = i

            while j >= interval and array[j - interval] > temp:

                array[j] = array[j - interval]

                j -= interval

            array[j] = temp

        interval //= 2

data = [59, 85, 35, 57, 535, 623, 4232, 31]

size = len(data)

shellSort(data, size)

print('Sorted Array in Ascending Order:')

print(data)
