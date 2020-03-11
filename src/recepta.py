#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Mòdul *recepta*
================

El mòdul *recepta* defineix un nou tipus d'objectes basats en els anteriors (els
Productes). Identifiquem una recepta amb el seu nom, o bé, pel seu conjunt de
Productes i les seves quantitats en grams.

La forma triada per representar-les ha sigut mitjançant els següents atributs:

\

nom [str, Públic]:
    És el nom de la recepta

ingredients [List, Privat]
    És una llista de tuples que enrergistra els ingredients de cada recepta. Cada
    tupla (p,q) codifica un producte p (atribut self.producte, heretat de la
    classe *Producte*) i la corresponent quantitat en grams q.

\


Definim la classe *Recepta* com mutable, ja que conté el mètode modificador,
*afegeix_ingredient*. A més a més, tenim altres mètodes per consultar
característiques concretes de la recepta, com ara *conte_ingredient*,
*quantitat_ingredient*, *pes_total* o *ingredients*. En total 5 mètodes únics
pels objectes tipus *Recepta*, explicats a continuació:
'''

from producte import*
from string import*


class Recepta(object):
    """
    -- Doctests conjunts de la classe *Recepta* --

    >>> r = Recepta('Pastís')
    >>> r.afegeix_ingredient('Nata', 200)
    [('Nata', 200)]
    >>> r.conte_ingredient('Nata')
    True
    >>> r.conte_ingredient('Xocolata')
    False
    >>> r.afegeix_ingredient('Xocolata', 100)
    [('Nata', 200), ('Xocolata', 100)]
    >>> r.pes_total()
    300
    >>> r.ingredients()
    ['Nata', 'Xocolata']
    >>> r.quantitat_ingredient('Xocolata')
    100
    >>> r.afegeix_ingredient('Maduixes', 50)
    [('Nata', 200), ('Xocolata', 100), ('Maduixes', 50)]
    >>> r.afegeix_ingredient('Xocolata', 200)
    [('Nata', 200), ('Maduixes', 50), ('Xocolata', 300)]
    >>> r.pes_total()
    550
    >>> r.ingredients()
    ['Nata', 'Maduixes', 'Xocolata']
    >>> r.conte_ingredient('Maduixes')
    True
    >>> r.conte_ingredient('Poma')
    False
    >>> r.quantitat_ingredient('Nata')
    200

    """

    def __init__(self, nom):
        self.nom = nom
        self._ingredients = []

    def afegeix_ingredient(self, p,q):
        '''
        *Mètode modificador*: Afegeix *q* grams del producte *p* a la recepta.\n

        Si la recepta ja contenia el Producte p, incrementa la seva quantitat
        en q grams.\n

        El paràmetre p, tot i ser inicialment un *string*, és processat i
        tractat com a objecte tipus Producte() al mètode (s'ha introduït com
        a *string* per comoditat).

        :param p: Nom del producte
        :type p: str
        :param q: Quantitat de producte en *q* grams
        :type q: int
        :returns: Una llista de tuples: [(p0, q0), (p1, q1), ...]
        :rtype: llista

        >>> r = Recepta('Pastis Xocolata')
        >>> r.afegeix_ingredient('Llet', 150)
        [('Llet', 150)]
        >>> r.afegeix_ingredient('xocolata', 200)
        [('Llet', 150), ('xocolata', 200)]
        >>> r.afegeix_ingredient('xocolata', 200)
        [('Llet', 150), ('xocolata', 400)]
        '''

        i = -5
        '''
        Aquest -5 el posem perquè fins al final hem vist un error MOLT GREU, teniem
        la variable i inicialitzada a 0, i si trobem dins d'una
        tupla un valor repetir el canviem, generant-nos "una senyal de canvi".

        L'error CRUCIAL, amb que ens hem topat ha sigut al repetir dos Productes
        seguits iguals, fent que el primer index sigui 0 el canviem a 0 peró la senyal
        no "haurà canviat" ja que el criteri decidit per canviar era que fos diferent a 0.

        Doncs, llavors, per aixó inicialitzem a qualsevol valor negatiu, o de diferentes
        maneres.
        '''
        for element in self._ingredients:
            if element[0] == p:
                j = element[1]
                i = self._ingredients.index(element)
                break

        if i != -5: # aixo tmb
            del self._ingredients[i]
            self._ingredients.append((Producte(p).producte, q + j))
            return self._ingredients

        else:
            self._ingredients.append((Producte(p).producte,q))
            return self._ingredients

    def conte_ingredient(self,p):
        '''
        :param p: Producte
        :type p: str
        :returns: Donat un producte, retorna True or False la recepta contingui el producte *p*
        :rtype: booleà

        >>> suc = Recepta('suc')
        >>> suc.afegeix_ingredient('taronja', 200)
        [('taronja', 200)]
        >>> suc.afegeix_ingredient('aigua', 1000)
        [('taronja', 200), ('aigua', 1000)]
        >>> suc.conte_ingredient('taronja')
        True
        >>> suc.conte_ingredient('aigua')
        True
        >>> suc.conte_ingredient('poma')
        False
        '''

        for element in self._ingredients:
            if element[0] == p:
                return True
        else:
            return False

    def quantitat_ingredient(self,p):
        '''
        :param p: Nom del producte
        :type p: str
        :returns: La quantitat de producte p en grams o 0 si no en conté
        :rtype: int

        >>> r = Recepta('Banana split')
        >>> r.afegeix_ingredient('Banana', 200)
        [('Banana', 200)]
        >>> r.afegeix_ingredient('Xocolata', 100)
        [('Banana', 200), ('Xocolata', 100)]
        >>> r.quantitat_ingredient('Banana')
        200
        >>> r.quantitat_ingredient('Blueberry')
        0
        >>> r.quantitat_ingredient('Xocolata')
        100

        '''
        for element in self._ingredients:
            if element[0] == p:
                return element[1]

        else:
            return 0


    def pes_total(self):
        '''
        :returns: Retorna el pes base total de la recepta en grams
        :rtype: list

        >>> llimonada = Recepta('llimonada')
        >>> llimonada.afegeix_ingredient('Llimona', 50)
        [('Llimona', 50)]
        >>> llimonada.afegeix_ingredient('Aigua', 1000)
        [('Llimona', 50), ('Aigua', 1000)]
        >>> llimonada.pes_total()
        1050
        '''

        return sum([tupla[1] for tupla in self._ingredients])


    def ingredients(self):
        '''
        :returns: Una llista d'ingredients de la recepta
        :rtype: llista

        >>> llimonada = Recepta('llimonada')
        >>> llimonada.afegeix_ingredient('Llimona', 50)
        [('Llimona', 50)]
        >>> llimonada.afegeix_ingredient('Aigua', 1000)
        [('Llimona', 50), ('Aigua', 1000)]
        >>> llimonada.ingredients()
        ['Llimona', 'Aigua']
        >>> llimonada.afegeix_ingredient('Sucre', 50)
        [('Llimona', 50), ('Aigua', 1000), ('Sucre', 50)]
        >>> llimonada.ingredients()
        ['Llimona', 'Aigua', 'Sucre']
        '''

        return [tupla[0] for tupla in self._ingredients]


if __name__ == '__main__':
    r = Recepta('gofre')
    print r.afegeix_ingredient('ous', 100)
    print r.afegeix_ingredient('ous', 100)
