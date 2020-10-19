# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:58:57 2020

@author: Cristian
"""

import math
from complex_numbers import complex_number
from complex_numbers import complex_cart
from complex_numbers import complex_polar


def sum_vect(A,B):
    if len(A) == len(B):
        ans = [complex_cart(0,0) for i in range(len(A))]
        for i in range(len(A)):
            ans[i] = A[i]+B[i]
        return ans
    else:
        return 'Los vectores no tienen la misma dimension'
def inv_adi(A):
    try:
        ans = [complex_cart(0,0)for i in range(len(A))]
        for i in range(len(A)):
            ans[i].a = -A[i].a 
            ans[i].b = -A[i].b
    except:
        ans = [0 for i in range(len(A))]
        for i in range(len(A)):
            ans[i] = -A[i]
    finally:
        return ans

def mul_esc_vect(A,B):
    ans = [[]for i in range(len(B))]
    for i in range(len(B)):
        ans[i]=A*B[i]
    return ans

def sum_mat_com(A,B):
    m_a = len(A)
    n_a = len(A[0])
    m_b= len(B)
    n_b= len(B[0])
    if m_a == m_b and n_a == n_b:
        ans = [[0 for i in range(len(A[0]))]for j in range(len(A))]
        for i in range(m_a):
            for j in range(n_a):
                ans[i][j] = A[i][j] + B[i][j]
        return ans
    else:
        return 'Error, la adicion de matrices no se puede'

def inv_adit_mat(A):
    m = len(A)
    n = len(A[0])
    ans = [[complex_cart(0,0)for i in range(n)]for i in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j].a = -A[i][j].a
            ans[i][j].b = -A[i][j].b
    return ans
def mult_esc_mat(A,B):
    m = len(B)
    n = len(B[0])
    ans = [[complex_cart(0,0)for i in range(n)]for i in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j]= A*B[i][j]
    return ans

def transpuesta(A):
    try:
        m = len(A)
        n = len(A[0])
        if n == 1 and m != 1:
            ans = [[]for i in range(m)]
            for i in range(m):
                ans[i] = A[i][0]
        else:
            ans = [[0 for j in range(m)]for i in range(n)]
            for i in range(n):
                for j in range(m):
                    ans[i][j] = A[j][i]
        return ans
    except:
        m = len(A)
        ans = [[]for i in range(m)]
        for i in range(m):
            ans[i] = [A[i]]
        return ans
    
def conjugado(A):
    try:
        m = len(A)
        n = len(A[0])
        if n == 1:
            ans = [[]for i in range(m)]
            for i in range(m):
                ans[i] = [A[i][0].conjugado()]
        else:
            ans = [[0 for j in range(n)]for i in range(m)]
            for i in range(m):
                for j in range(n):
                    ans[i][j] = A[i][j].conjugado()
        return ans
    except TypeError:
        m = len(A)
        ans = [[]for i in range(m)]
        for i in range(m):
            ans [i] = A[i].conjugado()

        return ans
def adjunta(A):
    ans = conjugado(A)
    ans = transpuesta(ans)
    return ans
   
def mult_mat(A,B):
    m_a = len(A)
    n_a = len(A[0])
    m_b= len(B)
    n_b= len(B[0])
    if n_a == m_b:
        ans = [[complex_cart(0,0) for i in range(len(B[0]))] for i in range (len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    ans[i][j] +=  A[i][k] * B[k][j]
        return ans
    else:
        return 'Error, el producto entre matrices no se puede'

def accion(A,B):
    m,n = len(A), len(A[0])
    m_b = len(B)
    if n == m_b:
        ans = [0  for i in range(m)]
        for i in range(m):
            suma = complex_cart(0,0)
            for j in range(n):
                suma += A[i][j]*B[j]
            ans[i] = suma
        return ans
    else:
        return 'La acción no se puede calcular '
    
def product_in(A,B):
    A = adjunta(A)
    n = len(A)
    m = len(B)
    if n == m:
        ans = complex_cart(0,0)
        for i in range(n):
            ans += A[i][0]*B[i]
    return ans



def norma_vect(A):
        ans = product_in(A,A)   
        ans = math.sqrt(ans.a)
        return round(ans,2)

def dist(A,B):
    return norma_vect(sum_vect(A,inv_adi(B)))

def unitary(A):
    A = mult_mat(A,adjunta(A))
    B = mult_mat(adjunta(A),A)
    ans = True
    if len(A) == len(A[0]):
        identy = [[complex_cart(0,0)for i in range (len(A[0]))]for j in range(len(A))]
        for i in range(len(A)):
            identy[i][i] = complex_cart(1,0)
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j].a == B[i][j].a and B[i][j].a ==identy[i][j].a and A[i][j].b == B[i][j].b and B[i][j].b ==identy[i][j].b:
                    ans = True
                else:
                    return False
        else:
            return ans
    else:
        print('La matriz no es cuadrada')

def hermitian(A):
    B = adjunta(A)
    ans = True
    if len(A) == len(A[0]):
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j].a == B[i][j].a and A[i][j].b == B[i][j].b:
                    ans = True
                else:
                    return False
        else:
            return ans
    else:
        print('La matriz no es cuadrada')
        return False
    
def product_tensor(A,B):
    try:
        m_a = len(A)
        n_a = len(A[0])
        m_b = len(B)
        n_b = len(B[0])
        m = m_a*m_b
        n = n_a*n_b
        ans = [[[]for j in range(n)]for i in range(m)]
        for j in range(m):
            for k in range(n):
                ans[j][k] = A[j//m_b][k//n_b]*B[j%m_b][k%n_b]
        return ans
    except:
        m = len(A)
        n = len(B)
        l = m*n
        ans = [[]for i in range(l)]
        for j in range(l):
            ans[j] = A[j//n]*B[j%n]
        return ans
    
                
    
                