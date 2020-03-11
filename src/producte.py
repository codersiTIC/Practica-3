#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Mòdul *producte*
=================

La classe *Producte* s'encarrega de definir aquests nous tipus d'objectes,
utilitzats als següents mòduls. Són les peces essencials d'aquest exercici 
(sense productes no hi hauria receptes ni, evidentment, receptari). 

Únicament conté un atribut, *self.producte*, corresponent al nom del producte
(representat com a *string*). 
'''

class Producte(object):
    """
    docstring for Product.

    >>> Producte('orange').producte
    'orange'
    >>> Producte('BanAna').producte
    'BanAna'
    >>> Producte('salt').producte
    'salt'
    """

    def __init__(self, producte):
        self.producte = producte

if __name__ == "__main__":

    print Producte('lemon').producte

    p = Producte('lemon')
    q = Producte('banana')
    n = Producte('fanta')

    print q.producte, p.producte, n.producte
