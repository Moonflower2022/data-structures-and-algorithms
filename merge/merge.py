import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'unsorted.txt')

file = open(filename, "r")

fileText = file.read()

def combine(list1, list2):
    ret = []
    i1 = 0
    i2 = 0
    while i1 + i2 != len(list1) + len(list2):
        if i1 == len(list1):
            for i in range(len(list2)):
                if i >= i2:
                    ret.append(list2[i])
            break
        elif i2 == len(list2):
            for i in range(len(list1)):
                if i >= i1:
                    ret.append(list1[i])
            break
        else:
            if list1[i1] < list2[i2]:
                ret.append(list1[i1])
                i1 += 1
                continue
            elif list2[i2] < list1[i1]:
                ret.append(list2[i2])
                i2 += 1
                continue
            else:
                ret.append(list1[i1])
                ret.append(list2[i2])
                i1 += 1
                i2 += 1
                continue
    return ret


def mergeSorted(list):
    if len(list) == 1:
        return list
    splitPoint = int(len(list)/2)
    #print(list[:splitPoint], list[splitPoint:])
    return combine(mergeSorted(list[:splitPoint]), mergeSorted(list[splitPoint:]))

numbers = [int(x) for x in  fileText.split("\n")]

print(mergeSorted(numbers))