import time
import math

unsorted = [
    [7, 1, 9, 3, 5, 6, 2, 5, 6],
    [-179, 630, -915, -621, -862, 351, 469, -933, -948, -127, 786, -259, 472, 168, -969, -978, -411, -537, -812, 44, -647, 544, -786, 34, -982, -601, -372, 105, 880, -979, -405, 327, 111, 322, -997, 127, 622, 673, 441, 213, -54, -341, -337, -527, 500, 151, -120, 12, -952, 861, 738, 497, -316, 733, -739, 549, 808, -886, -336, 348, 562, 14, 494, 71, 744, 652, 700, -285, -787, -939, -814, 313, 705, -583, -479, -334, 164, -661, -858, 678, -509, 160, 271, 399, 450, -141, -49, 920, -64, 468, 283, -965, 726, 400, -814, 175, 858, -498, 131, -948, -39, -667, 692, 968, 327, -909, -80, 897, -761, -574, -125, 20, 185, -284, -439, 593, -259, -839, 126, 177, -456, -768, 540, 7, -655, -350, 387, 244, -239, 349, 439, 381, 46, 775, 263, 863, -502, 858, -472, 39, 476, 369, -686, 66, -927, -562, -35, 921, 295, -437, 858, 598, -344, 1, 809, -564, -57, -495, -96, -110, 637, -851, 331, -244, -430, -49, -301, 771, 240, -295, 757, 510, 759, 740, 667, 209, 647, 653, 90, 727, 317, 462, 863, 393, -287, -860, -442, -563, 64, 863, 103, 968, 219, 677, 523, -842, 84, -936, -677, 74, -969, -439, -477, 621, 195, 694, 859, 228, -491, -818, 694, -616, 197, 911, 697, 568, 870, 501, 223, 535, -600, 97, -429, 334, -974, 198, 711, -988, -526, -811, 240, 676, 89, -437, 447, 399, 669, 971, -96, -312, 360, 307, -377, 277, -141, 880, -936, -370, 88, 832, 25, 351, -971, -761, 342, 77, 472, -819, -991, -1000, -402, 329, 680, -774, -748, 119, -897, -356, -970, 914, 273, -107, 930, -312, -531, -327, -71, -510, 852, 39, 59, -717, 178, -751, 447, -819, -38, 237, -924, -588, -682, -120, 204, 125, -349, -696, 829, 302, -985, -227, -788, 415, 525, -500, -819, 416, 719, 84, -922, 30, 254, -113, 846, -838, -710, -435, 140, -58, 613, 156, 558, -881, -955, 6, -415, 623, 171, -44, 739, 587, -573, 522, 817, -174, -597, -462, 197, -121, 399, -945, -184, -336, 67, 352, -587, 290, 351, -855, 595, -839, -168, -375, 32, 391, 755, -900, -507, -702, -139, -101, -220, 368, 741, 245, -963, -427, -110, 132, 455, 738, -136, 692, -23, 338, -882, 549, 971, 275, 243, 746, 216, 447, -792, 754, 923, -375, 202, 216, 792, -936, 679, 236, -347, -660, 230, 682, 857, 706, -196, 148, -66, 357, -50, 72, 537, 774, 547, -621, -188, 497, 303, 172, 180, -73, -44, -449, 497, 528, 676, -787, -216, -774, 477, -709, -470, 319, 299, -61, -796, 734, 999, -285, -6, 368, 331, 857, 260, -261, -715, -27, -171, -816, -999, -408, 516, 777, 384, 419, -516, -53, 233, 930, -413, -312, -205, -153, -153, -674, 66, -887, 914, 951, 135, -933, -801, -271, 540, -259, -732, 517, 448, 362, -793, 818, -849, 522, -824, 608, -458, -929, -446, -926, -448, -127, 78, -620, 522, -383, -970, 493, 158, 560, -210, 967, -123, -478, -652, -476, -575, -819],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [],
    [1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 1],
    [3, 3, 3, 3, 3, 3, 3 ,3 ,3 , 3, 3, 3],
    [math.pi, math.e, math.log(2), 1],
    [0.1, 6.5, 0.9, 0.2, 0.1, -0.5, -0.9, 9.4, 10.3, 10, 78, 92, -10.7]
]

# incorrect implementation

'''
def insertion_sorted(arr):
    if type(arr) != list:
        raise Exception("Not of type 'list', type was ", str(type(arr)))
    if len(arr) <= 1:
        return arr
    sorted_arr = [arr[-1]]
    for i in range(2, len(arr) + 1):
        for j in range(len(sorted_arr)):
            if arr[-i] <= sorted_arr[j]: # find the place that arr[-i] should go
                sorted_arr.insert(j, arr[-i])  # insert it
                break
            if j == len(sorted_arr) - 1: sorted_arr.append(arr[-i]) # if no one is bigger than ours, then we must be biggest
    return sorted_arr
'''

def insertion_sorted(arr):
    if type(arr) != list:
        raise Exception("Not of type 'list', type was ", str(type(arr)))
    if len(arr) <= 1:
        return arr

    arr_copy = [*arr] # make copy
    for i in range(1, len(arr_copy)): # dont include 0 bc first element is alr good
        j = i
        while j >= 1: # if j is 0 then j - 1 would be bad
            if arr_copy[j] < arr_copy[j-1]: # check if we are smaller than previous
                arr_copy[j], arr_copy[j-1] = arr_copy[j-1], arr_copy[j] # switch
                j = j - 1
                continue # keep checking
            break # otherwise, we are in good place so check next
    return arr_copy

for arr in unsorted:
    print("array: ", arr)
    assert insertion_sorted(arr) == sorted(arr), f"oopsie poopie the lists are not the same :( my sort: {insertion_sorted(arr)} != python sort: {sorted(arr)}"
    start_time = time.time()
    insertion_sorted(arr)
    print("my function running time: ", time.time() - start_time)

    start_time = time.time()
    sorted(arr)
    print("python function running time: ", time.time() - start_time)

print("test cases passed!")


            
