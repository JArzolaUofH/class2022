#  Justine Arzola 1804667 homework 4


def selection_sort_descend_trace(integerlist):  # def to take the integer list and sort it in order
    for i in range(len(integerlist) - 1):
        pos = i
        for j in range(i + 1, len(integerlist)):  # create the nested loops to output list
            if integerlist[pos] < integerlist[j]:
                pos = j
        integerlist[i], integerlist[pos] = integerlist[pos], integerlist[i]
        for value in integerlist:
            print(value, end=" ")
        print()
    return integerlist


if __name__ == "__main__":
    integerlist = []

    integerlist = [int(x) for x in input("").split()]
    selection_sort_descend_trace(integerlist)  # call to def statement to do sorting of list
