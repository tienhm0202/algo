"""
Practice sorting algorithm, include

1. Bubble sort - bubble()
2. Selection sort - selection()
3. Insertion sort - insertion()
4. Merge sort - merge_sort()
5. Quick sort - quick_sort()
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


def merge_sort(data, start=0, end=None):
    """
    Sorting by merge algorithm

    @param data: list of items to sort
    """
    if end is None:
        end = len(data)

    if start < end - 1:
        middle = int((start + end) / 2)

        left = merge_sort(data, start, middle)
        right = merge_sort(data, middle, end)
        return _merge(left, right)


def _merge(left, right):
    """
    Merge two ordered part in one
    """
    data = list()
    left_i = 0
    right_i = 0
    while True:
        left_val = None
        if left and left_i < len(left):
            left_val = left[left_i]
        elif right:
            return data + right[right_i:]
        else:
            return data

        right_val = None
        if right and right_i < len(right):
            right_val = right[right_i]
        elif left:
            return data + left[left_i:]
        else:
            return data

        if left_val and right_val:
            if left_val < right_val:
                data.append(left_val)
                left_i += 1
            else:
                data.append(right_val)
                right_i += 1


def quick_sort(data):
    """
    Quick sort

    @param data: list of items to sort
    """
    if len(data) <= 1:
        return data

    middle_key = int(len(data) / 2)
    middle_val = data[middle_key]

    # Break a list in two list separated by middle value
    bigger = list()
    smaller = list()
    equal = list()

    for value in data:
        if value > middle_val:
            bigger.append(value)
        elif value < middle_val:
            smaller.append(value)
        else:
            equal.append(value)

    return quick_sort(smaller) + equal + quick_sort(bigger)
