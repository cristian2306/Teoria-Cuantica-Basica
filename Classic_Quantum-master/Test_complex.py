# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:15:15 2020

@author: Cristian
"""


import unittest
import math
from complex_numbers import complex_number
from complex_numbers import complex_cart
from complex_numbers import complex_polar
import mat_op

class Test_complex(unittest.TestCase):
    
    def setUp(self):
        """Genera números complejos, unos en forma polar, y otros en forma
        cartesiana"""
        self.complex_a = complex_cart(1,2)
        self.complex_b = complex_cart(2,4)
        self.complex_c = complex_cart(-6,2)
        self.complex_d = complex_cart(-5,-8)
        self.complex_e = complex_cart(0,0)
        self.complex_f = complex_cart(1,1)
        self.complex_h = complex_cart(1/2,3/4)
        self.complex_A = complex_polar(8,(3*math.pi)/4)
        self.complex_B = complex_polar(3,(23*math.pi)/22)
        self.complex_C = complex_polar(24,(3*math.pi)/5)
        self.complex_D = complex_polar(4.47,1.11)
        self.mat_num_B = [[1,2,3],[1,2,3],[1,2,3]]
        self.mat_num_A = [[1,2],[1,2],[1,2]]
        self.vect_num_C = [1,2,3]
        self.vect_num_D = [1,2,3,4]            
        self.mat_comp_a = [[complex_cart(1,2),complex_cart(1,2)],[complex_cart(1,2),complex_cart(1,2)],[complex_cart(1,2),complex_cart(1,2)]]            
        self.mat_comp_b = [[complex_cart(1,1),complex_cart(2,2),complex_cart(3,3)],[complex_cart(1,1),complex_cart(2,2),complex_cart(3,3)],[complex_cart(1,1),complex_cart(2,2),complex_cart(3,3)]]            
        self.vect_comp_c = [complex_cart(1,1),complex_cart(2,2),complex_cart(3,3)]            
        self.vect_comp_d = [complex_cart(1,1),complex_cart(2,2),complex_cart(3,3),complex_cart(4,4)]
        
    def test_add(self):
        """Test de la función suma de números complejos"""
        self.assertEqual(str(self.complex_a + self.complex_b),str((3,6)))
        self.assertEqual(str(self.complex_a + self.complex_a),str((2,4)))
        self.assertEqual(str(self.complex_a + self.complex_e), str((1,2)))
        self.assertEqual(str(self.complex_h + self.complex_h), str((1.0,1.5)))

    def test_sub(self):
        """Test de la función resta de números complejos"""
        self.assertEqual(str(self.complex_a - self.complex_a), str((0,0)))
        self.assertEqual(str(self.complex_b - self.complex_c), str((8,2)))
        self.assertEqual(str(self.complex_c - self.complex_b),str((-8,-2)))
        self.assertEqual(str(self.complex_d - self.complex_a) , str((-6,-10)))
        self.assertEqual(str(self.complex_a - self.complex_e), str((1,2)))
        
    def test_mul(self):
        """Test de la función producto de números complejos"""
        self.assertEqual(str(self.complex_a * self.complex_b) , str((-6,8)))
        self.assertEqual(str(self.complex_c * self.complex_f), str((-8,-4)))
        self.assertEqual(str(self.complex_d * self.complex_c), str((46,38)))
        self.assertEqual(str(self.complex_h * self.complex_b) , str((-2.0,3.5)) )        
        
    def test_div(self):
        """Test de la función cociente de números complejos"""
        self.assertEqual(str(self.complex_f / self.complex_h), str((0.8,-0.16)))
        self.assertEqual(str(self.complex_a / self.complex_a), str((0.62,0.0)))
        self.assertEqual(str(self.complex_c / self.complex_f), str((-0.8,1.6)))
        self.assertEqual(str(self.complex_h / self.complex_b), str((0.24, -0.03)))
        
    def test_mod(self):
        """Test de lafunción módulo de números complejos"""
        self.complex_a_b = (self.complex_a + self.complex_b)
        self.assertEqual(str(self.complex_a_b.mod()), str(6.71))
        self.complex_ab = self.complex_a * self.complex_b
        self.assertEqual(str(self.complex_ab.mod()),str(10.0))
        self.assertEqual(str(self.complex_a.mod()), str(2.24))
        self.assertEqual(str(self.complex_b.mod()), str(4.47))
        self.assertEqual(str(self.complex_e.mod()), str(0.0))
        self.assertEqual(str(self.complex_f.mod()), str(1.41))
        
    def test_conjugado(self):
        """Test de la función conjugado de números complejos"""
        self.assertEqual(str(self.complex_a.conjugado()),str((1,-2)))
        self.assertEqual(str(self.complex_b.conjugado()),str((2,-4)))
        self.assertEqual(str(self.complex_c.conjugado()),str((-6,-2)))
        self.assertEqual(str(self.complex_d.conjugado()),str((-5,8)))
        self.assertEqual(str(self.complex_e.conjugado()),str((0,0)))
        self.assertEqual(str(self.complex_f.conjugado()),str((1,-1)))
        self.assertEqual(str(self.complex_h.conjugado()),str((1/2,-3/4)))
          
    def test_polar(self):
        """Test de la función polar de números complejos"""
        self.assertEqual(str(self.complex_a.polar()),str((2.24,1.11)))
        self.assertEqual(str(self.complex_h.polar()),str((0.90,0.98)))
        self.assertEqual(str(self.complex_f.polar()),str((1.41,0.79)))
        self.assertEqual(str(self.complex_b.polar()),str((4.47,1.11)))
        
    def test_phase(self):
        """"Test de la función fase de números complejos"""
        self.assertEqual(str(self.complex_a.phase()),str(1.11))
        self.assertEqual(str(self.complex_h.phase()),str(0.98))
        self.assertEqual(str(self.complex_f.phase()),str(0.79))
        self.assertEqual(str(self.complex_b.phase()),str(1.11))
    
    def test_cart(self):
        """Test de la función cartesiana de números complejos"""
        self.assertEqual(str(self.complex_A.cart()),str((-5.66,5.66)))
        self.assertEqual(str(self.complex_B.cart()),str((-2.97,-0.43)))
        self.assertEqual(str(self.complex_C.cart()),str(((-7.42,22.83))))
        self.assertEqual(str(self.complex_D.cart()),str((1.99,4.0)))
         
    def test_sum_vect(self):
        self.assertEqual(mat_op.sum_vect(self.vect_num_C,self.vect_num_C),[2,4,6])
        self.assertEqual(str(mat_op.sum_vect(self.vect_comp_d,self.vect_comp_d)),'[2 + 2i, 4 + 4i, 6 + 6i, 8 + 8i]')
        
    def test_inv_adi(self):
        self.assertEqual(mat_op.inv_adi(self.vect_num_C),[-1,-2,-3])
        self.assertEqual(str(mat_op.inv_adi(self.vect_comp_d)),'[-1 + (-1i), -2 + (-2i), -3 + (-3i), -4 + (-4i)]')
        
    def test_mul_esc_vect(self):
        self.assertEqual(mat_op.mul_esc_vect(5,self.vect_num_C),[5,10,15])
        self.assertEqual(str(mat_op.mul_esc_vect(complex_cart(5,5),self.vect_comp_d)),'[0 + 10i, 0 + 20i, 0 + 30i, 0 + 40i]')
    
    def test_sum_mat_com(self):
        self.assertEqual(str(mat_op.sum_mat_com(self.mat_comp_a,self.mat_comp_a)),'[[2 + 4i, 2 + 4i], [2 + 4i, 2 + 4i], [2 + 4i, 2 + 4i]]')
        self.assertEqual(str(mat_op.sum_mat_com(self.mat_comp_b,self.mat_comp_b)),'[[2 + 2i, 4 + 4i, 6 + 6i], [2 + 2i, 4 + 4i, 6 + 6i], [2 + 2i, 4 + 4i, 6 + 6i]]')
        
    def test_inv_adit_mat(self):
        self.assertEqual(str(mat_op.inv_adit_mat(self.mat_comp_a)),'[[-1 + (-2i), -1 + (-2i)], [-1 + (-2i), -1 + (-2i)], [-1 + (-2i), -1 + (-2i)]]')
        self.assertEqual(str(mat_op.inv_adit_mat(self.mat_comp_b)),'[[-1 + (-1i), -2 + (-2i), -3 + (-3i)], [-1 + (-1i), -2 + (-2i), -3 + (-3i)], [-1 + (-1i), -2 + (-2i), -3 + (-3i)]]')
        
    def test_mult_esc_mat(self):
        self.assertEqual(str(mat_op.mult_esc_mat(complex_cart(5,2),self.mat_comp_a)),'[[1 + 12i, 1 + 12i], [1 + 12i, 1 + 12i], [1 + 12i, 1 + 12i]]')
        self.assertEqual(str(mat_op.mult_esc_mat(complex_cart(5,2),self.mat_comp_b)),'[[3 + 7i, 6 + 14i, 9 + 21i], [3 + 7i, 6 + 14i, 9 + 21i], [3 + 7i, 6 + 14i, 9 + 21i]]')
        
    def test_transpuesta(self):
        self.assertEqual(mat_op.transpuesta(self.mat_num_A),[[1, 1, 1], [2, 2, 2]])
        self.assertEqual(str(mat_op.transpuesta(self.mat_comp_a)),'[[1 + 2i, 1 + 2i, 1 + 2i], [1 + 2i, 1 + 2i, 1 + 2i]]')
        self.assertEqual(mat_op.transpuesta(self.vect_num_D),[[1], [2], [3], [4]])
        self.assertEqual(str(mat_op.transpuesta(self.vect_comp_d)),'[[1 + 1i], [2 + 2i], [3 + 3i], [4 + 4i]]')
        
    def test_conjugado(self):
        self.assertEqual(str(mat_op.conjugado(self.mat_comp_a)),'[[1 + (-2i), 1 + (-2i)], [1 + (-2i), 1 + (-2i)], [1 + (-2i), 1 + (-2i)]]')
        self.assertEqual(str(mat_op.conjugado(self.mat_comp_b)),'[[1 + (-1i), 2 + (-2i), 3 + (-3i)], [1 + (-1i), 2 + (-2i), 3 + (-3i)], [1 + (-1i), 2 + (-2i), 3 + (-3i)]]')
        self.assertEqual(str(mat_op.conjugado(self.vect_comp_c)),'[1 + (-1i), 2 + (-2i), 3 + (-3i)]')
        self.assertEqual(str(mat_op.conjugado(self.vect_comp_d)),'[1 + (-1i), 2 + (-2i), 3 + (-3i), 4 + (-4i)]')
        
    def test_adjunta(self):
        self.assertEqual(str(mat_op.adjunta(self.mat_comp_a)),'[[1 + (-2i), 1 + (-2i), 1 + (-2i)], [1 + (-2i), 1 + (-2i), 1 + (-2i)]]')
        self.assertEqual(str(mat_op.adjunta(self.mat_comp_b)),'[[1 + (-1i), 1 + (-1i), 1 + (-1i)], [2 + (-2i), 2 + (-2i), 2 + (-2i)], [3 + (-3i), 3 + (-3i), 3 + (-3i)]]')
        self.assertEqual(str(mat_op.adjunta(self.vect_comp_c)),'[[1 + (-1i)], [2 + (-2i)], [3 + (-3i)]]')
        self.assertEqual(str(mat_op.adjunta(self.vect_comp_d)),'[[1 + (-1i)], [2 + (-2i)], [3 + (-3i)], [4 + (-4i)]]')
        
    def test_mult_mat(self):
        self.assertEqual(str(mat_op.mult_mat(self.mat_comp_b,self.mat_comp_a)),'[[-6 + 18i, -6 + 18i], [-6 + 18i, -6 + 18i], [-6 + 18i, -6 + 18i]]')
        self.assertEqual(str(mat_op.mult_mat(self.mat_comp_b,mat_op.transpuesta(self.mat_comp_b))),'[[0 + 28i, 0 + 28i, 0 + 28i], [0 + 28i, 0 + 28i, 0 + 28i], [0 + 28i, 0 + 28i, 0 + 28i]]')
        self.assertEqual(str(mat_op.mult_mat(self.mat_comp_a,mat_op.transpuesta(self.mat_comp_a))),'[[-6 + 8i, -6 + 8i, -6 + 8i], [-6 + 8i, -6 + 8i, -6 + 8i], [-6 + 8i, -6 + 8i, -6 + 8i]]')
        
    def test_accion(self):
        a = [[complex_cart(-1,0),complex_cart(1,1),complex_cart(0,0)],[complex_cart(2,-1),complex_cart(0,0),complex_cart(1,0)],[complex_cart(0,0),complex_cart(1,-1),complex_cart(0,1)]]
        b = [complex_cart(1,0),complex_cart(1,1),complex_cart(0,1)]
        self.assertEqual(str(mat_op.accion(a,b)),'[-1 + 2i, 2 + 0i, 1 + 0i]')
        
    def test_product_in(self):
        a = [complex_cart(1,0),complex_cart(0,1),complex_cart(1,-3)]
        b = [complex_cart(2,1),complex_cart(0,1),complex_cart(2,0)]
        self.assertEqual(str(mat_op.product_in(a,b)),'(5, 7)')
        
    def test_norma_vect(self):
        a = [complex_cart(3.4,4.6),complex_cart(2.2,-7.1)]
        b = [complex_cart(8.2,5.3),complex_cart(8.1,-8.0)]
        self.assertEqual(mat_op.norma_vect(a),9.38)
        self.assertEqual(mat_op.norma_vect(b),15.0)
        
    def test_dist(self):
        self.assertEqual(mat_op.dist(self.vect_comp_c,mat_op.inv_adi(self.vect_comp_c)),10.58)
        self.assertEqual(mat_op.dist(self.vect_comp_d,mat_op.inv_adi(self.vect_comp_d)),15.49)
    
    def test_unitary(self):
        a = [[complex_cart(0,0)for i in range(3)]for i in range(3)]
        for i in range(3):
            a[i][i] = complex_cart(0,1)
        self.assertEqual(mat_op.unitary(a),True)
        self.assertEqual(mat_op.unitary(self.mat_comp_b),False)
        
    def test_hermitian(self):
        a = [[complex_cart(5,0),complex_cart(3,7)],[complex_cart(3,-7),complex_cart(2,0)]]
        self.assertEqual(mat_op.hermitian(a),True)
        self.assertEqual(mat_op.hermitian(self.mat_comp_b),False)
        
    def test_product_tensor(self):
        self.assertEqual(str(mat_op.product_tensor(self.vect_num_C,self.vect_num_D)),'[1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12]')
        self.assertEqual(str(mat_op.product_tensor(self.mat_num_A,self.mat_num_B)),'[[1, 2, 3, 2, 4, 6], [1, 2, 3, 2, 4, 6], [1, 2, 3, 2, 4, 6], [1, 2, 3, 2, 4, 6], [1, 2, 3, 2, 4, 6], [1, 2, 3, 2, 4, 6], [1, 2, 3, 2, 4, 6], [1, 2, 3, 2, 4, 6], [1, 2, 3, 2, 4, 6]]')
        self.assertEqual(str(mat_op.product_tensor(self.vect_comp_c,self.vect_comp_d)),'[0 + 2i, 0 + 4i, 0 + 6i, 0 + 8i, 0 + 4i, 0 + 8i, 0 + 12i, 0 + 16i, 0 + 6i, 0 + 12i, 0 + 18i, 0 + 24i]')
        self.assertEqual(str(mat_op.product_tensor(self.mat_comp_a,self.mat_comp_b)),'[[-1 + 3i, -2 + 6i, -3 + 9i, -1 + 3i, -2 + 6i, -3 + 9i], [-1 + 3i, -2 + 6i, -3 + 9i, -1 + 3i, -2 + 6i, -3 + 9i], [-1 + 3i, -2 + 6i, -3 + 9i, -1 + 3i, -2 + 6i, -3 + 9i], [-1 + 3i, -2 + 6i, -3 + 9i, -1 + 3i, -2 + 6i, -3 + 9i], [-1 + 3i, -2 + 6i, -3 + 9i, -1 + 3i, -2 + 6i, -3 + 9i], [-1 + 3i, -2 + 6i, -3 + 9i, -1 + 3i, -2 + 6i, -3 + 9i], [-1 + 3i, -2 + 6i, -3 + 9i, -1 + 3i, -2 + 6i, -3 + 9i], [-1 + 3i, -2 + 6i, -3 + 9i, -1 + 3i, -2 + 6i, -3 + 9i], [-1 + 3i, -2 + 6i, -3 + 9i, -1 + 3i, -2 + 6i, -3 + 9i]]')
        


if __name__== '__main__':
    unittest.main()

