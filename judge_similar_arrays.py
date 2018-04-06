"""
There are two arrays. 

int arr1[5] = { 3, 5, 2, 5, 2} 
int arr2[5] = { 2, 3, 5, 5, 2} 

The arrays will be called similar if they contain same number of elements equally. 

You are not allowed to use sorting and hashtable.
"""


def judge(arr1, arr2):
    result = False
    if arr1 and arr2 and len(arr1) == len(arr2):
        arr2_cp = arr2[:]
        for e in arr1:
            arr2_cp.remove(e)

        if len(arr2_cp) == 0:
            result = True

    return result


if __name__ == "__main__":
    arr1 = input("Please input the first array:\n")
    arr2 = input("Please input the second array:\n")
    is_similar = judge(arr1, arr2)
    print "The two arrays are " + ("" if is_similar else "not ") + "similar"
    print arr1
    print arr2

