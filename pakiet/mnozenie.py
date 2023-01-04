import numpy as np
def my_dot(a,b):
    """Moduł mający na celu wymnożyć dwie macierze podane w postaci argumentów"""
    result = np.empty((a.shape[0],b.shape[1]))
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            result[i][j] = sum([x*y for x,y in zip(a[i,:],b[:,j])])
    return result