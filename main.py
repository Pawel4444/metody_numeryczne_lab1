import numpy as np
import scipy
import math

def cylinder_area(r:float,h:float):
    if  isinstance(r, float) and isinstance(h, float) and r >= 0 and h >= 0:
        pp = np.pi * r**2
        pb = 2 * np.pi * r * h
        pc = 2*pp + pb

        return pc
    else:
        return np.nan


def fib(n:int):
    if n == 1:
        return np.array([1])
    if n>0 and isinstance(n, int):
        a = 1
        b = 1        
        wek = np.array([1, 1])
        for i in range(1, n-1):
            a, b = b, a + b
            wek = np.append(wek, b)
        return wek.reshape([1,n])
    else:
        return None



def matrix_calculations(a:float):
    M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    if a == 0:
        Minv = np.NaN
    else:
        Minv = np.linalg.inv(M)
    Mt = M.T
    Mdet = np.linalg.det(M)
    return (Minv, Mt, Mdet)


    

def custom_matrix(m:int, n:int):
    
    
    if m>0 and n>0 and isinstance(m, int) and isinstance(n, int):
        wynik = np.zeros((m,n))
        for i in range(m):
            for j in range(n):
                if i>j:
                    wynik[i, j] = i
                else:
                    wynik[i, j] = j
        return wynik
    else:
        return None


