from random import randint, random
import numpy as np
from InsertionSorting import insertion_sort, List
from time import time

#averagecase= [randint(1,10000) for  in range(1000)]
#bestcase= sorted(averagecase)
#worstcase= sorted(averagecase, reverse=True)
avaragecase = List
bestcase = np.sort(avaragecase)
worstcase = bestcase[::-1]
def test_SelectionWorst():
    start= time()
    assert np.array_equal( insertion_sort(np.copy(worstcase)) , bestcase)
    print(str(time()-start))

def test_SelectionBest():
    start= time()
    assert np.array_equal( insertion_sort(np.copy(bestcase)) , bestcase)
    print(str(time()-start))
    
def test_SelectionAvg():
    start= time()
    assert np.array_equal( insertion_sort(np.copy(avaragecase)) , bestcase)
    print(str(time()-start))