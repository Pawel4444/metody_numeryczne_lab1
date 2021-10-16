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
        return None


def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if n == 1 or n ==2:
        return 1
    elif n>2:
        return fib(n-1)+fib(n-2)
    else:
        return None
#print(fib(6))

def matrix_calculations(a:float):
    M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    Minv = np.linalg.inv(M)
    Mt = M.T
    Mdet = np.linalg.det(M)
    return (Minv, Mt, Mdet)


    

def custom_matrix(m:int, n:int):
    wynik = np.zeros((m,n))
    
    if m>0 and n>0:
        for i in range(m):
            for j in range(n):
                if i>j:
                    wynik[i, j] = i
                else:
                    wynik[i, j] = j
        return wynik
    else:
        return None
#print("lalaa")       
#print(custom_matrix(4,6))

