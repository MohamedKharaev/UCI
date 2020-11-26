from typing import List
import math

def prob_2_find_local_minimum(nums : List[int]) -> int:
    '''
    Use divide and conquer to find the index of ANY local minimum in nums, 
    where the first and last elements of nums are infinity (and thus cannot be local minima).

    Let i = prob_2_find_local_minimum(nums)
    Then a correct implementation should return an i that satisfies
        0 < i < len(nums) - 1
        nums[i] <= nums[i - 1]
        nums[i] <= nums[i + 1]
    Your tests for this function can be exactly these expressions. Use assert as below.

    It is easy to see that if the first and last elements are infinity, 
    there must be AT LEAST ONE local minimum. You are not required to find any particular one.
    Any one that satisfies the conditions above will be considered correct.

    NOTE: We are not asking you for the number itself, but its index. 
    The same number may appear in several places: a local minimum in some, and not in others.
    e.g. [inf, 8, 3, 1, 9, 3, 7, inf]
          0    1  2  3  4  5  6  7
          3 appears at index 2 but is not a local minimum because 3 > 1
          3 also appears at index 5 and is a local minimum because 3 < 9, 3 < 7
    Your algorithm must be strictly more efficient than the obvious linear time algorithm.

    NOTE: In Python, math.inf is a special value that satisfies math.inf >= x for any int x.
    '''
    assert len(nums) >= 3 # there is at least one non-infinite value
    assert nums[0] == math.inf
    assert nums[-1] == math.inf # -1: last element
    assert all(num != math.inf for num in nums[1:-1]) # only the first and last elements are inf
    return _prob_2_find_local_minimum(nums);

def _prob_2_find_local_minimum(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0;
    if len(nums) == 2:
        return 0 if nums[0] < nums[1] else 1;
    mid = len(nums) // 2;
    if nums[mid - 1] > nums[mid] and nums[mid + 1] > nums[mid]:
        return mid;
    else:
        if nums[mid - 1] < nums[mid]:
            return _prob_2_find_local_minimum(nums[ :mid]);
        else:
            return mid + _prob_2_find_local_minimum(nums[mid: ]);

    '''
    Asymptotic Notation: O(logn)
    Recurrence Relation: T(n) = aT(n/2) + O(logn)

    Explanation:

    1) Check the middle number and see if it is a local minima
    2) if Left of middle is smaller, then there must be a local minima in the left side  n 
    3) if Right or middle is smaller, then there must be a local minima in the right side
    4) Repeat until local minima is found
    '''


'''
This is a public interface your solution for problem 3 must use.
You cannot assume anything else about the internals of this class.
So if s is a Selector object, you can only call len(s) and s.get_kth_largest(k) for various k.

You may want to implement this class yourself for your tests.
You can do this simply by just sorting the items in descending order in some list l,
and then returning l[k].
'''
class Selector:
    def __init__(self, nums : List[float]) -> None: 
        '''
            This constructor is provided just to show you what kinds of objects Selector stores.
            You may not assume anything about the attributes of Selector objects.
            nums may be unsorted.
            e.g. you cannot assume 'nums' is one of the members.
        '''
        pass

    def __len__(self) -> int:
        '''
            Return the number of items in the selector.
            The __len__ signature means you can call len(s) on selector objects s,
            just like you can with lists and other built in data structures.
        '''
        pass
    
    def get_kth_largest(self, k : int) -> float:
        '''
            Suppose the elements sorted in descending order are given by a list l.
            Return l[k].
            If s is a Selector object, then
            s.get_kth_largest(0) is the largest element in the data set and
            s.get_kth_largest(len(s) - 1) is the smallest element in the data set.

            If k < 0 or k >= len(s), IndexError is thrown.
        '''
        pass

def prob_3_find_median_of_combined_data_set(s1 : Selector, s2 : Selector) -> float:
    '''
        Return the median element of the values in s1 and s2 using O(log n) queries.
        Note: Remember that c log n = O(log n) for any c > 0
        If 
        s1 contains elements s1_0 < s1_1 < ... < s1_n,
        s2 contains elements s2_0 < s2_1 < ... < s2_n,
        l is the sorted list of the above items [l_0, l_1, ... , l_(2n)],
        Note that the total number of elements must be even.
        then this function returns
            (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2

        Of course, since you can only discover elements using Selector.get_kth_largest,
        and you must use at most O(log n) queries, you cannot construct l explicitly.
        This description is just meant to tell you what your task is.
    '''

    return _prob_3_find_median_of_combined_data_set(s1, s2, len(s1), 0, 0);

def _prob_3_find_median_of_combined_data_set(s1 : Selector, s2 : Selector, n: int, s1_offset: int, s2_offset: int) -> float:
    if n == 0:
        return 0;
    if n == 1:
        return (s1.get_kth_largest(s1_offset) + s2.get_kth_largest(s2_offset)) / 2
    if n == 2:
        return (min(s1.get_kth_largest(s1_offset), s2.get_kth_largest(s2_offset)) + max(s1.get_kth_largest(s1_offset + 1), s2.get_kth_largest(s2_offset + 1))) / 2
    m1 = median(s1, n, s1_offset)
    m2 = median(s2, n, s2_offset)
    n = (n // 2) + 1
    if m2 > m1:
        s2_offset = (len(s1) - n - s1_offset)
    elif m1 > m2:
        s1_offset = (len(s1) - n - s2_offset)
    else:
        return m1
    return _prob_3_find_median_of_combined_data_set(s1, s2, n, s1_offset, s2_offset)

def median(s: Selector, n: int, offset):
    if n % 2 == 0:
        return (s.get_kth_largest(n // 2 + offset) + s.get_kth_largest((n // 2) + 1 + offset)) / 2
    else:
        return s.get_kth_largest(n//2 + offset)

