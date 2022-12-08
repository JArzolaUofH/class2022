# Justine Arzola 1804667 homework 4
import math

num_calls = 0
def partition(user_ids, first, second):  # to determine if a swap is necessary

    beginning = first
    end = second

    claim = user_ids[math.floor((first + second) / 2)]

    while beginning <= end:

        while user_ids[beginning] < claim:
            beginning = beginning + 1

        while user_ids[end] > claim:
            end = end - 1

        if beginning <= end:
            tmp = user_ids[beginning]
            user_ids[beginning] = user_ids[end]
            user_ids[end] = tmp
            beginning = beginning + 1
            end = end - 1

    return beginning


def quicksort(user_ids, first, second):  # algorithm to recursively sort high and low partitions
    global num_calls
    num_calls = num_calls + 1
    if first < second:
        mid = partition(user_ids, first, second)
        quicksort(user_ids, first, mid - 1)
        quicksort(user_ids, mid, second)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls) # to print the number of calls to quicksort

    for x in user_ids:  # for the print sorted user ids
        print(x)
