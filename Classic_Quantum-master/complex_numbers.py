# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:40:20 2020

@author: Cristian
"""
import math

class complex_number(object):
   

    def __init__(self):
        self.a = 0
        self.b = 0
        self.r = 0
        self.tetha = 0
    

    
class complex_cart(complex_number):
    
    def __repr__(self):
        if self.b < 0:
            return str(self.a) + " + (" + str(self.b) + "i)"
        else:
            return str(self.a) + " + " + str(self.b)+'i'

    def __init__(self,x,y):
        self.a = x
        self.b = y
    
    def __str__(self):
        string = (self.a,self.b)
        return str(string)
    
    def __add__(self,self_1):
        """Suma dos números complejos en forma cartesiana"""
        ans_a = round(self.a + self_1.a,2)
        ans_b = round(self.b + self_1.b,2)
        ans = complex_cart(ans_a,ans_b)
        return ans
    
    def __sub__(self,self_1):
        """Resta dos números complejos en forma carteisana"""
        ans_a = self.a - self_1.a
        ans_b = self.b - self_1.b
        ans = complex_cart(ans_a,ans_b)
        return ans
    
    def __mul__(self, self_1):
        "Realiza el producto de dos números complejos"""
        ans_a = round((self.a * self_1.a) - (self.b * self_1.b),2)
        ans_b = round((self.a * self_1.b) + (self.b * self_1.a),2)
        ans = complex_cart(ans_a,ans_b)
        return ans
    
    def __truediv__(self, self_1):
        """Realiza el cociente de dos números complejos"""
        ans = complex_number()
        ans_1 = (self.a * self_1.a) + (self.b * self_1.b)
        ans_2 = (self.b * self_1.a) - (self.a * self_1.b)
        module = (self.b**2)+(self_1.b**2)
        ans_a = round(ans_1/module,2)
        ans_b = round(ans_2/module,2)
        ans = complex_cart(ans_a,ans_b)
        return ans
    
    def mod(self):
        """Cálcula el módulo de un número complejo"""
        return round(math.sqrt((self.a**2)+(self.b**2)),2)
    
    def conjugado(self):
        """Cálcula el conjugado de un número complejo"""
        ans_a = self.a
        ans_b = -self.b
        ans = complex_cart(ans_a,ans_b)
        return ans
    
    def polar(self):
        """Retorna la forma polar de un número complejo"""
        mod = self.mod()
        tetha = self.phase()
        ans = complex_polar(mod,tetha)
        return ans
    
    def phase(self):
        """Retorna la fase de un número complejo"""
        return round((math.atan2(self.b,self.a)),2)
    
class complex_polar(complex_number):
    
    def __repr__(self):
        return(str((self.r,self.tetha)))
    
    def __init__(self,r,tetha):
        self.r = r
        self.tetha = tetha
        
    def cart(self):
        """Retorna la forma cartesiana de un número complejo"""
        real = round((self.r*math.cos(self.tetha)),2)
        imag = round((self.r*math.sin(self.tetha)),2)
        ans = complex_cart(real,imag)
        return ans
    
    def __srt__(self):
        string = (self.r,self.tetha)
        return str(string)



        

