# Required: Python 3.5+
from typing import List

'''
Note about built in data structures:

You are only allowed to use 'list' and 'tuple' objects for this submission.

You are explicitly forbidden from using 'set', 'dict', and any other built in data structures,
as well as any other data structures available from external packages.

You may however implement new classes that use 'list' and 'tuple' objects.

Our test harness will disable the instantiation of any forbidden data structures and you may
receive little to no points for offending implementations (at our discretion).
'''

def prob_3_find_profs(diff : List[float], humor : List[int]) -> List[int]: 
    '''
        The ith professor has difficulty diff[i] and humor humor[i]
        return the list of indexes of professors as required by the problem statement
    '''
    assert len(diff) == len(humor)
    result = [];
    maxI = humor.index(max(humor));
    for x in range(len(diff)):
        if diff[x] <= diff[maxI]:
            result.append(x);
    return result;

'''
public interface
you do not need to include or implement this class for your submission. 
we will have an implementation on our side that we will use.
if you would like to implement it for testing or practice, you are free to do so.
the definition below is intended just to show you the interface you should adhere to in your submission
'''
class MaxHeap:
    def max(self) -> int:
        '''Return the max value without modifying contents of heap.'''
        pass

    def removeMax(self) -> int:
        '''Remove max value, restore heap property, and return the value'''
        pass

    def isEmpty(self) -> bool:
        pass

    # Other methods omitted

def prob_4_max_heaps_intersect(mh1 : MaxHeap, mh2 : MaxHeap) -> bool:
    '''
        Return True iff mh1 and mh2 have some element in common.
        The only access you have to each heap is through its public interface.
    '''
    while not mh1.is_empty() and not mh2.is_empty():
        mh1_max = mh1.max();
        mh2_max = mh2.max();
        if mh1_max == mh2_max:
            return True;
        else:
            if mh1_max < mh2_max:
                mh2.removeMax();
            else:
                mh1.removeMax();
    return False;
    '''
        Answer: The reason this algorithm is O(n log n) is because removeMax is a
                function that takes log n time. It is performed at most once for every
                value in mh1 and mh2 if there is no matching key. Therefore, a log n
                function is called n times by this function, making it O(n log n).
    '''

def prob_5a_phone_number_duplicated(phone_nums : List[str]) -> bool:
    '''
        Phone numbers are strs of length 7 (no separators).
        Example: '3134895'

        Return True if at least one phone number is duplicated. Otherwise return False.
    '''
    phone_nums2 = [0] * 10000000;
    for num in phone_nums:
        if phone_nums2[int(num)] == 1:
            return True;
        phone_nums2[int(num)] += 1;
    return False;

def prob_5b_get_phone_numbers_sorted(phone_nums : List[str]) -> List[str]:
    '''
        Phone numbers are strs of length 7 (no separators).
        Example: '3134895'

        Return a new independent list of distinct phone numbers in sorted order.
        If a phone number is duplicated, only include it once in the list.
    '''
    phone_nums2 = [None] * 10000000;
    for num in phone_nums:
        phone_nums2[int(num)] = num;
    ret = [];
    for pn in phone_nums2:
        if pn != None:
            ret.append(pn);
    return ret;
