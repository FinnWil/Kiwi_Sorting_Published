import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Data = pd.read_csv('data.csv')
weight = Data[['Weight(kg)']]
weight = np.array(weight)
plt.plot (weight)

weightSorted = weight

def insertion_sort(A): 


        for i in range(1, len(A)): 

            a = A[i] 


            j = i - 1 

            while j >= 0 and a < A[j]: 
                A[j + 1] = A[j] 
                j -= 1 

            A[j + 1] = a 

        return A

insertion_sort(weightSorted)

plt.plot(weightSorted)
plt.ylabel("Weight(kg)")
plt.legend(["Unsorted", "Sorted"])
plt.show()