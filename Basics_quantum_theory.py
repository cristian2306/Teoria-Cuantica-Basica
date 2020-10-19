# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:17:18 2020

@author: Cristian
"""
import math
from complex_numbers import complex_number
from complex_numbers import complex_cart
from complex_numbers import complex_polar
import mat_op
import Classic_Quantum as Classic
import numpy as np

def Assembling(particles):
    '4.5.2'
    ans = mat_op.product_tensor(particles[0][0],particles[1][0])
    for i in range(2,len(particles)):
        ans = mat_op.product_tensor(ans, particles[i][0])
    x = 0
    for i in range(len(particles)):
        ans_1 = 1
        for j in range(i):
            ans_1 *= len(particles[j][0])
        x += particles[i][1]*ans_1
    return Quantum_states(x,mat_op.transpuesta(ans),None)

def Identy(n):
    ans = [[complex_cart(0,0) for i in range(n)] for j in range(n)]
    for i in range(n):
        ans [i][i] = complex_cart(1,0)
    return ans


def Quantum_states (x, ket,ket_a):
    ket = mat_op.transpuesta(ket)
    if ket_a is None:
        ans = []
        for i in range(len(ket)):
            prob = (round((ket[i].mod()**2),2))/(round((mat_op.norma_vect(ket)**2),2))
            ans += [prob]
        return ans[x]
    else: 
        ket_a = mat_op.transpuesta(ket_a)
        ans = mat_op.product_in(ket_a,ket)
        norma_ket = mat_op.norma_vect(ket)
        norma_ket_a = mat_op.norma_vect(ket_a)
        b = norma_ket*norma_ket_a
        return complex_cart(ans.a/b, ans.b/b)
    
def Observables (observable, ket):
    
    if mat_op.hermitian(observable):
        
        ans = mat_op.mult_mat(observable, ket)
        media = mat_op.product_in(mat_op.transpuesta(ans), mat_op.transpuesta(ket))

        
        identy = mat_op.mult_esc_mat(media,Identy(len(observable)))
        operador = mat_op.sum_mat_com(observable,mat_op.inv_adit_mat(identy))
        operador_1 = mat_op.mult_mat(operador,operador)
        ket_operador = mat_op.transpuesta(mat_op.mult_mat(operador_1,ket))
        var  = mat_op.product_in(mat_op.transpuesta(ket),ket_operador)
        return var.a
    
    else:
        
        return None
 
def Measuring(observable, ket):
    observable = [[complex(observable[i][j].a,observable[i][j].b) for j in range(len(observable[i]))] for i in range(len(observable))]
    A = np.array(observable)
    eigenvalues, eigenvects  = np.linalg.eig(A)
    c = []
    b = []
    for i in range(len(eigenvects)):
        d = []
        b += [complex_cart(eigenvalues[i].real, eigenvalues[i].imag)]
        for j in range(len(eigenvects[i])):
            z = eigenvects[i][j]
            d += [complex_cart(z.real, z.imag)]
        c += [d]
    if ket is None:
        return (b,c)
    else:
        prob = [] 
        for i in range(len(b)):
            prob += [(mat_op.product_in(mat_op.transpuesta(ket),c[i])).mod()**2]
        return (b,c,prob)
    
def Dynamics(n, U_n, state):
    if mat_op.unitary(U_n): 
        U = U_n
        for i in range(n):
            ans  = mat_op.mult_mat(U,state)
            U = mat_op.mult_mat(U,U_n)
        prob = ans
        prob = [round(ans[i][0].mod()**2,2) for i in range(len(ans))]
        return prob
    else :
        return 'Matriz no unitaria'
    
def Problem(x):
    if x == '4.3.1':
        observable  = [
            [complex_cart(0,0),complex_cart(1,0)],
            [complex_cart(1,0),complex_cart(0,0)]
            ]
        ket = [[complex_cart(1,0)],[complex_cart(0,0)]]
        ans = Measuring(observable,ket)
        return ans[1]
    elif x == '4.3.2':
        observable  = [
            [complex_cart(0,0),complex_cart(1,0)],
            [complex_cart(1,0),complex_cart(0,0)]
            ]
        ket = [[complex_cart(1,0)],[complex_cart(0,0)]]
        ans = Measuring(observable,ket)
        value = ans[0][0]*complex_cart(ans[2][0],0)+ans[0][1]*complex_cart(ans[2][1],0)
        print(value)

        ans_1 = mat_op.mult_mat(observable, ket)
        media = mat_op.product_in(mat_op.transpuesta(ans_1), mat_op.transpuesta(ket))
        print(media)
        print('El valor de la distribucion hallado es igual al que se obtiene en el calculo de la media')
        return(media)
    elif x == '4.4.1':
        U_1 = [
            [complex_cart(0,0),complex_cart(1,0)],
            [complex_cart(1,0),complex_cart(0,0)]
            ]
        U_2 = [
            [complex_cart(math.sqrt(2/4),0),complex_cart(math.sqrt(2/4),0)],
            [complex_cart(math.sqrt(2/4),0),complex_cart(-math.sqrt(2/4),0)]
            ]
        print(mat_op.unitary(U_1,), mat_op.unitary(U_2))
        print('Las dos matrices son unitarias')
        U_3 = mat_op.mult_mat(U_1,U_2)
        print(mat_op.unitary(U_3))
        print('El producto de las matrices es unitario')
        return[mat_op.unitary(U_3)]
        
    elif x == '4.4.2':
        U_n = [
        [complex_cart(0,0),complex_cart(1/math.sqrt(2),0),complex_cart(1/math.sqrt(2),0),complex_cart(0,0)],
        [complex_cart(0,1/math.sqrt(2)),complex_cart(0,0),complex_cart(0,0),complex_cart(1/math.sqrt(2),0)],
        [complex_cart(1/math.sqrt(2),0),complex_cart(0,0),complex_cart(0,0),complex_cart(0,1/math.sqrt(2))],
        [complex_cart(0,0),complex_cart(1/math.sqrt(2),0),complex_cart(-1/math.sqrt(2),0),complex_cart(0,0)]
        ]
        state = state = mat_op.transpuesta([complex_cart(1,0),complex_cart(0,0),complex_cart(0,0),complex_cart(0,0)])
        ans = Dynamics(3,U_n,state)
        return ans[3]
    elif x == '4.5.2':
        return 'hola'
    else:
        return 'EL ejercicio no fue propuesto'


    
    
    
    
    
    