from random import randint, random
import numpy as np
from BubbleSorting import bubbleSort, List
from time import time

# avaragecase= [randint(1,10000) for _ in range(1000)]
# bestcase= sorted(avaragecase)
# worstcase= sorted(avaragecase, reverse=True) 
avaragecase = List
bestcase = np.sort(avaragecase)
worstcase = bestcase[::-1]
def test_BubbleWorst():
    start= time()
    assert np.array_equal( bubbleSort(np.copy(worstcase)) , bestcase)
    print(str(time()-start))

def test_BubbleBest():
    start= time()
    assert np.array_equal( bubbleSort(np.copy(bestcase)) , bestcase)
    print(str(time()-start))
    
def test_BubbleAvg():
    start= time()
    assert np.array_equal( bubbleSort(np.copy(avaragecase)) , bestcase)
    print(str(time()-start))