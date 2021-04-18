# Q1. Given a positive integer N. The task is to write a Python program to check if the number is prime or not.
def is_prime(n: int) -> bool:
    if n < 2:
        return False

    # (1) sqrt of n
    # (2) 23: [2,3,5,7,11,13,15,17]
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# DO NOT ALTER BELOW.
assert is_prime(2)
assert not is_prime(15)
assert is_prime(7907)
assert not is_prime(-1)
assert not is_prime(0)


# Q2 Write a function rotate(ar[], d) that rotates arr[] of size n by d elements.
# Input ar = [1,2,3,4,5,6,7], d = 2
# Output [3,4,5,6,7,1,2]

def rotate(ar: [int], d: int) -> [int]:
    # [21 76543]
    # [3456712]
    d = d % len(ar)
    inplace_reverse(ar, 0, d - 1)
    inplace_reverse(ar, d, len(ar) - 1)
    inplace_reverse(ar, 0, len(ar) - 1)
    return ar


def inplace_reverse(ar: [int], start: int, end: int):
    while start < end:
        ar[start], ar[end] = ar[end], ar[start]
        start += 1
        end -= 1


# DO NOT ALTER BELOW.
assert rotate([1, 2, 3, 4, 5, 6, 7], 2) == [3, 4, 5, 6, 7, 1, 2]
assert rotate([1, 2, 3], 4) == [2, 3, 1]


# Q3. Selection sort - implement a workable selection sort algorithm
# https://www.runoob.com/w3cnote/selection-sort.html 作为参考
# Input students would be a list of [student #, score], sort by score ascending order.

def selection_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j][1] <= arr[min_index][1]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# DO NOT ALTER BELOW.
assert selection_sort([]) == []
assert selection_sort([[1, 100], [2, 70], [3, 95], [4, 66], [5, 98]]) == [[4, 66], [2, 70], [3, 95], [5, 98], [1, 100]]


# Q4. Convert a list of Tuples into Dictionary

# tips: copy operation - copy by value, copy by reference

def convert(tup: (any), di: {any, any}) -> None:
    for i in range(0, len(tup), 2):
        di[tup[i]] = tup[i + 1]
    # Do NOT RETURN di, EDIT IN-PLACE


# DO NOT ALTER BELOW.
expected_dict = {}
convert((), expected_dict)
assert expected_dict == {}

convert(('key1', 'val1', 'key2', 'val2'), expected_dict)
assert expected_dict == {'key1': 'val1', 'key2': 'val2'}
