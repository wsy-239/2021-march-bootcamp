#!/usr/bin/env python
# coding: utf-8

# # 注意
# 
# # Copy this file and rename Assignment2-{first_name}.ipynb 
# 
# ### 解题步骤
# 
# * understand question and test case
# * check input
# * algorithm
# * check return
# 
# Instruction: make sure your code pass the assertion statements

# Q1. Given a positive integer N. The task is to write a Python program to check if the number is prime or not.
def is_prime(n:int)->bool:
    if n <= 1 and isinstance(n, int):
        return False
    for i in range (2,n):
        if n% i== 0:
            return False
        else:
            return True
        
# DO NOT ALTER BELOW.
assert is_prime(2)
assert not is_prime(15)
assert is_prime(7907)
assert not is_prime(-1)
assert not is_prime(0)        


# In[ ]:


# Q2 Write a function rotate(ar[], d) that rotates arr[] of size n by d elements.
# Input ar = [1,2,3,4,5,6,7], d = 2
# Output [3,4,5,6,7,1,2]
def rotate(ar:[int], d:int)->list:
    if d == 0:
        return ar
    else:
        ar[:] = ar[-d: len(ar)] + ar[0: -d]
    return ar

# DO NOT ALTER BELOW.
assert rotate([1,2,3,4,5,6,7], 4) == [3,4,5,6,7,1,2]
assert rotate([1,2,3], 4) == [2,3,1]


# In[ ]:


#Q3 Selection sort - implement a workable selection sort algorithm
# https://www.runoob.com/w3cnote/selection-sort.html 作为参考
# Input students would be a list of [student #, score], sort by score ascending order.
def selection_sort(arr:[[int]])->list:
    b=sorted(arr,key=lambda x:x[1])
    return b

# DO NOT ALTER BELOW.
assert selection_sort([]) == []
assert selection_sort([[1, 100], [2, 70], [3, 95], [4, 66], [5, 98]]) == [[4, 66], [2, 70], [3, 95], [5, 98], [1, 100]]


# In[ ]:


# Q4. Convert a list of Tuples into Dictionary

# tips: copy operation - copy by value, copy by reference
# 123, String, immutable (copy by value)
# mutable, list, dict... (copy by reference)
def convert(tup:(any), di:{any,any}) -> None:
    for i in range(0,len(tup),2):
        di[tup[i]] = tup[i+1]
    pass

# DO NOT ALTER BELOW.
expected_dict = {}
convert((), expected_dict)
assert expected_dict == {}

convert(('key1', 'val1', 'key2', 'val2'), expected_dict)
assert expected_dict == {'key1': 'val1', 'key2': 'val2'} 


# In[ ]:


# Q5. 研究为什么 Python dict 可以做到常数级别的查找效率，将答案写在 Assignment2-{firstname}.ipynb
dict对象的存储结构采用的是散列表(哈希表)，哈希表是一个用于存储Key-Value键值对的集合，使用哈希表可以进行非常快速的查找操作，查找时间为常数，同时不需要元素排列有序。

