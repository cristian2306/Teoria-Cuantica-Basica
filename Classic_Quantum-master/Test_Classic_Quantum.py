# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:53:03 2020

@author: Cristian
"""

import unittest
import math
from complex_numbers import complex_number
from complex_numbers import complex_cart
from complex_numbers import complex_polar
import mat_op
import Classic_Quantum as classic

class Test_Classic_Quantum(unittest.TestCase):
    
    def setUp(self):
        self.mat_bool = [[False, False, False, False, False, False],
                    [False, False, False, False, False, False],
                    [False, True, False, False, False, True],
                    [False, False, False, True, False, False],
                    [False, False, True, False, False, False],
                    [True, False, False, False, True, False]]
        self.vect_bool=[False, False, True, False, False, False]
        self.mat_real = [[0,1/6,5/6],[1/3,1/2,1/6],[2/3,1/3,0]]
        self.vect_real = ([1/6,1/6,2/3])
        A = [[complex_cart(0,0) for i in range(8)] for j in range(8)]
        A[1][0]=complex_cart(1/math.sqrt(2),0) 
        A[2][0]=complex_cart(1/math.sqrt(2),0)
        A[3][1]=complex_cart(-1/math.sqrt(6),1/math.sqrt(6))
        A[3][3]=complex_cart(1,0)
        A[4][1]=complex_cart(-1/math.sqrt(6),-1/math.sqrt(6))      
        A[4][4]=complex_cart(1,0)
        A[5][1]=complex_cart(1/math.sqrt(6),-1/math.sqrt(6))
        A[5][2]=complex_cart(-1/math.sqrt(6),1/math.sqrt(6))
        A[5][5]=complex_cart(1,0)
        A[6][2]=complex_cart(-1/math.sqrt(6),-1/math.sqrt(6))
        A[6][6]=complex_cart(1,0)
        A[7][2]=complex_cart(1/math.sqrt(6),-1/math.sqrt(6))
        A[7][7]=complex_cart(1,0)
        self.mat_compleja = A
        B = [[complex_cart(0,0) for i in range(3)]for j in range(3)]
        B[0][0]= complex_cart(1/math.sqrt(2),0)
        B[1][0]=complex_cart(0,-1/math.sqrt(2))
        B[0][1]=complex_cart(1/math.sqrt(2),0)
        B[1][1]=complex_cart(0,1/math.sqrt(2))
        B[2][2]=complex_cart(0,-1)
        self.complex_mat = B
        self.complex_vect = [complex_cart(1/math.sqrt(3),0),complex_cart(0,2/math.sqrt(15)),complex_cart(math.sqrt(2/5),0)]
        
    def test_Probabilistic_system(self):
        self.assertEqual(classic.Probabilistic_system(self.mat_bool,5,self.vect_bool),
                         [[False], [False], [False], [False], [False], [True]])
        self.assertEqual(classic.Probabilistic_system(self.mat_real,1,self.vect_real),[[0.58],[0.25],[0.17]])
        
    def Quantum_system(self):
        self.assertEqual(classic.Quantum_system(self.complex_mat,1,self.complex_vect),[[0.3], [0.3], [0.4]])
        
    
    def test_exp_real_slit(self):
        self.assertEqual(classic.exp_real_slit(3,5),[[0.0],[0.0],[0.0],[0.0],[0.07],[0.07],
                                                     [0.07],[0.13],[0.13],[0.07],[0.13],[0.13],
                                                     [0.07],[0.07],[0.07]])
   
    def test_exp_complex_slit(self):
        self.assertEqual(classic.exp_complex_slit(self.mat_compleja),[[0.0], [0.0], [0.0], [0.17], [0.17], [0.0], [0.17], [0.17]])
        
        


if __name__== '__main__':
    unittest.main()

        
