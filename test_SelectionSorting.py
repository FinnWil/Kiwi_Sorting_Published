from random import randint, random
import numpy as np
from SelectionSorting import selectionSort, List
from time import time

# avaragecase= [randint(1,10000) for _ in range(1000)]
# bestcase= sorted(avaragecase)
# worstcase= sorted(avaragecase, reverse=True) 
avaragecase = List
bestcase = np.sort(avaragecase)
worstcase = bestcase[::-1]
def test_SelectionWorst():
    start= time()
    assert np.array_equal( selectionSort(np.copy(worstcase), len(worstcase)) , bestcase)
    print(str(time()-start))

def test_SelectionBest():
    start= time()
    assert np.array_equal( selectionSort(np.copy(bestcase), len(bestcase)) , bestcase)
    print(str(time()-start))
    
def test_SelectionAvg():
    start= time()
    assert np.array_equal( selectionSort(np.copy(avaragecase), len(avaragecase)) , bestcase)
    print(str(time()-start))