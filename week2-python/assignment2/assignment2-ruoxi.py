# Instruction: make sure your code pass the assertion statements

# Q1. Given a positive integer N. The task is to write a Python program to check if the number is prime or not.
def is_prime(n: int) -> bool:
    return n >= 1 and (0 not in (n%i for i in range(2,n)))
      


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
    n = d%len(ar)
    return ar[n:]+ar[0:n]
  

# DO NOT ALTER BELOW.
assert rotate([1,2,3,4,5,6,7], 2) == [3,4,5,6,7,1,2]
assert rotate([1,2,3], 4) == [2,3,1]





# Q3 Selection sort - implement a workable selection sort algorithm
# https://www.runoob.com/w3cnote/selection-sort.html 作为参考
# Input students would be a list of [student #, score], sort by score ascending order.

def selection_sort(arr: [[int]]) -> [[int]]:
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j][1] < arr[min][1]:
                min = j
        if i != min:
            arr[i], arr[min] = arr[min], arr[i]
    return arr


# DO NOT ALTER BELOW.
assert selection_sort([]) == []
assert selection_sort([[1, 100], [2, 70], [3, 95], [4, 66], [5, 98]]) == [[4, 66], [2, 70], [3, 95], [5, 98], [1, 100]]






# Q4. Convert a list of Tuples into Dictionary

# tips: copy operation - copy by value, copy by reference

def convert(tup: (any), di: {any, any}) -> None: 
    for i in range(int(len(tup)/2)):
      di[tup[2*i]]=tup[2*i+1]
    pass
    # Do NOT RETURN di, EDIT IN-PLACE
    
    
# DO NOT ALTER BELOW.
expected_dict = {}
convert((), expected_dict)
assert expected_dict == {}

convert(('key1', 'val1', 'key2', 'val2'), expected_dict)
assert expected_dict == {'key1': 'val1', 'key2': 'val2'}




# Q5. 研究为什么 Python dict 可以做到常数级别的查找效率，将答案写在 assignment2-{firstname}.ipynb

dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。dict采取的是这种方法。

具体来说，dict的查找通过hash来实现。哈希算法将任意长度的二进制值映射为较短的固定长度的二进制值，这个小的二进制值称为哈希值。
哈希值是一段数据唯一且极其紧凑的数值表示形式。如果散列一段明文而且哪怕只更改该段落的一个字母，随后的哈希都将产生不同的值。
要找到散列为同一个值的两个不同的输入，在计算上是不可能的，所以数据的哈希值可以检验数据的完整性,一般用于快速查找和加密算法.

dict会把所有的key变成hash 表，然后将这个表进行排序，这样，通过data[key]去查data字典中一个key的时候，python会先把这个key hash成一个数字.
然后拿这个数字到hash表中看没有这个数字，如果有，拿到这个key在hash表中的索引，拿到这个索引去与此key对应的value的内存地址那取值就可以了。

参考链接：
https://www.liaoxuefeng.com/wiki/1016959663602400/1017104324028448
https://blog.csdn.net/lm236236/article/details/96484203
