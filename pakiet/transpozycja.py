"""Moduł pozwalający nam transponować macierz."""
import numpy as np
def my_transpose(x):
    """Funckjapozwalająca nam transponować macierz, którą podajemy jako argument x"""
    result = np.empty((x.shape[1],x.shape[0]))  
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            result[j][i]=x[i][j]
    return result