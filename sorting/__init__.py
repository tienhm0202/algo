"""
Practice sorting algorithm, include

1. Bubble sort - bubble()
2. Selection sort - selection()
3. Insertion sort - insertion()
"""


def bubble(data):
    """
    Represent bubble sorting

    @param data: is a list of items to sort
    """
    last_unsorted_item = len(data)
    time_swap = 0
    while True:
        swapped = False
        for i in data:
            if data.index(i) >= last_unsorted_item - 1:
                break

            if i > data[data.index(i) + 1]:
                # Swap i and i + 1
                index_i = data.index(i)
                index_j = index_i + 1
                data[index_i], data[index_j] = data[index_j], data[index_i]

                time_swap += 1
                swapped = True
        if not swapped:
            break

        last_unsorted_item -= 1

    return time_swap


def selection(data):
    """
    Sortting by selection algorithm

    @param data: list of items to sort
    """
    time_swap = 0
    for i in range(0, len(data)):
        minimum = data[i]
        for j in range(i + 1, len(data)):
            if data[j] < minimum:
                minimum = data[j]
                time_swap += 1

        data[i] = minimum
    return time_swap


def insertion(data):
    """
    Sorting by insertion algorithm

    @param data: list of items to sort
    """
    time_swap = 0
    sorted_list = list()
    for i in range(0, len(data)):
        is_break = False
        for item in sorted_list:
            if data[i] < item:
                sorted_list.insert(sorted_list.index(item), data[i])
                time_swap += 1
                is_break = True
                break

        if not is_break:
            sorted_list.append(data[i])
            time_swap += 1

    return sorted_list, time_swap
