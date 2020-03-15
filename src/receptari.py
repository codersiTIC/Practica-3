#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Module *receptari*
==================

El mòdul *receptari.py* conté la classe *Receptari*, la qual està fonamentalment
formada per múltiples objectes de tipus *Recepta*. S'ha decidit representar als
objectes de la classe mitjançant dos atributs principals:

receptes [dict, Privat]
    És un diccionari en el que la clau correspon al nom de totes les receptes
    del receptari i el valor correspon a l’objecte Recepta corresponent.

productes [dict, Privat]
    És un diccionari en el que la clau correspon al nom de tots els productes
    que intervenen en el receptari i el valor correspon a l’objecte Producte
    corresponent.

* *El receptari inicialment no conté cap recepta ni producta*.\n
La classe *Receptari* és de tipus mutable, ja què conté els mètodes modificadors
*afegeix_recepta*, *afegeix_producte* i *afegeix_ingredient_recepta*. La resta
de mètodes no modificadors de la classe són: *receptes_ingredient*, *receptes*, *ingredients* i *recepta*. En total, 7 mètodes específics dels objectes tipus *Receptari*, explicats a continuació:
'''

from recepta import*

class Receptari(object):
    """
    -- Doctests conjunts de la classe *Recepta* --

    >>> r = Receptari()
    >>> r.afegeix_recepta('Pastis Xocolata')
    >>> r.afegeix_recepta('Pastis Xocolata')
    La recepta ja existeix
    >>> r.afegeix_recepta('Gofre')
    >>> r.afegeix_producte('Llet')
    >>> r.afegeix_producte('Ous')
    >>> r.afegeix_ingredient_recepta('Gofre', 'Llet', 500)
    >>> r.afegeix_ingredient_recepta('Pastis Xocolata', 'Llet', 200)
    >>> r.afegeix_ingredient_recepta('Pastis Xocolata', 'Ous', 200)
    >>> r.receptes_ingredient('Llet')
    ['Gofre', 'Pastis Xocolata']
    >>> r.receptes_ingredient('Ous')
    ['Pastis Xocolata']
    >>> r.receptes()
    ['Gofre', 'Pastis Xocolata']
    >>> r.ingredients()
    ['Ous', 'Llet']
    >>> r.recepta('Pastis Xocolata')
    [('Llet', 200), ('Ous', 200)]
    >>> r.recepta('Gofre')
    [('Llet', 500)]
    """

    def __init__(self):
        self._receptes = dict()
        self._productes = dict()


    def afegeix_recepta(self,n):
        '''
        Modificador. Afegeix una recepta de nom n al receptari, és a dir, afegeix al dicionari de clau [nomr] una instància de Receptari(nomr).

        :param n: Nom de la recepta
        :type n: str

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_recepta('Pastis Xocolata')
        >>> Receptari.afegeix_recepta('Pastis Xocolata')
        La recepta ja existeix
        >>> Receptari.afegeix_recepta('Gofres')
        '''

        if self._receptes.has_key(n):
            print "La recepta ja existeix"
        else:
            self._receptes[n] = Recepta(n)


    def afegeix_producte(self, nomp):
        '''
        Afegeix un nou Producte de nom nomp.

        :param nomp: Nom del producte
        :type nomp: str

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_producte('Farina')
        >>> Receptari.afegeix_producte('Ous')
        >>> Receptari.afegeix_producte('Farina')
        El producte ja existeix
        '''

        if nomp in self._productes.keys():
            print "El producte ja existeix"
        else:
            self._productes[nomp] = Producte(nomp)


    def afegeix_ingredient_recepta(self,nomr,nomp,q):
        '''
        Afegeix q grams de l’ingredient de nom nomp a la recepta de nom nomr.

        :param nomr: Nom de la recepta
        :type nomr: str
        :param nomp: Nom del pecepta
        :type nomp: str
        :param q: Quantitat de producte en gr
        :type q: int

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_producte('Farina')
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Farina', 500)
        La recepta < Gofre > no existeix
        >>> Receptari.afegeix_recepta('Gofre')
        >>> Receptari.afegeix_producte('Ous')
        >>> Receptari.afegeix_producte('Farina')
        El producte ja existeix
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Farina', 500)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Ous', 500)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Llet', 500)
        El producte < Llet > no existeix
        '''
        if (nomr not in self._receptes.keys()):
            print ("La recepta < %s > no existeix")%(nomr)
        else:
            if (nomp not in self._productes.keys()):
                print ("El producte < %s > no existeix")%(nomp)
            else:
                self._receptes[nomr].afegeix_ingredient(nomp, q)

    def receptes_ingredient(self,nomp):
        '''
        :param nomp: Nom del producte
        :type nomp: str
        :returns: Una llista de noms de receptes que contenen l'ingredient *nomp*
        :rtype: llista

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_recepta('Gofre')
        >>> Receptari.afegeix_recepta('Pastis Xocolata')

        >>> Receptari.afegeix_producte('Farina')
        >>> Receptari.afegeix_producte('Ous')
        >>> Receptari.afegeix_producte('Llet')
        >>> Receptari.afegeix_producte('Sucre')

        >>> Receptari.afegeix_ingredient_recepta('Pastis Xocolata', 'Farina', 700)
        >>> Receptari.afegeix_ingredient_recepta('Pastis Xocolata', 'Llet', 500)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Farina', 500)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Llet', 300)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Sucre', 200)

        >>> Receptari.receptes_ingredient('Farina')
        ['Pastis Xocolata', 'Gofre']
        >>> Receptari.receptes_ingredient('Llet')
        ['Pastis Xocolata', 'Gofre']
        >>> Receptari.receptes_ingredient('Sucre')
        ['Gofre']
        >>> Receptari.receptes_ingredient('Ous')
        []

        '''
        l = []
        for recepta in self._receptes.values():
            if nomp in recepta.ingredients():
                l.append(recepta.nom)
        return l


    def receptes(self):
        '''
        :returns: La llista dels noms de les receptes que conté el receptari
        :rtype: llista

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_recepta('Gofre')
        >>> Receptari.afegeix_recepta('Pastis Xocolata')
        >>> Receptari.afegeix_recepta('Paella')
        >>> Receptari.afegeix_recepta('Hamburguesa de bacalla')

        >>> Receptari.receptes()
        ['Hamburguesa de bacalla', 'Pastis Xocolata', 'Gofre', 'Paella']
        '''

        return self._receptes.keys()


    def ingredients(self):
        '''
        :returns: La llista dels noms de productes del receptari
        :rtype: llista

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_recepta('Gofre')

        >>> Receptari.afegeix_producte('Farina')
        >>> Receptari.afegeix_producte('Ous')
        >>> Receptari.afegeix_producte('Llet')
        >>> Receptari.afegeix_producte('Llevat')

        >>> Receptari.ingredients()
        ['Ous', 'Llevat', 'Farina', 'Llet']
        '''
        return self._productes.keys()


    def recepta(self,nomr):
        '''
        :param nomr: Nom de la recepta
        :type nomr: str
        :returns: Retorna una llista de parells (nomp, q) cadascun dels quals representa un ingredient de la recepta **nomr**. Cada parell agrega el nom del producte nomr i el pes necessari en **q** grams.

        :rtype: llista

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_recepta('Gofre')
        >>> Receptari.afegeix_recepta('Pastis Xocolata')

        >>> Receptari.afegeix_producte('Farina')
        >>> Receptari.afegeix_producte('Ous')
        >>> Receptari.afegeix_producte('Llet')
        >>> Receptari.afegeix_producte('Sucre')

        >>> Receptari.afegeix_ingredient_recepta('Pastis Xocolata', 'Farina', 700)
        >>> Receptari.afegeix_ingredient_recepta('Pastis Xocolata', 'Llet', 500)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Farina', 500)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Llet', 300)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Sucre', 200)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Sucre', 200)

        >>> Receptari.receptes_ingredient('Farina')
        ['Pastis Xocolata', 'Gofre']
        >>> Receptari.receptes_ingredient('Llet')
        ['Pastis Xocolata', 'Gofre']
        >>> Receptari.receptes_ingredient('Sucre')
        ['Gofre']
        >>> Receptari.receptes_ingredient('Ous')
        []

        >>> Receptari.recepta('Gofre')
        [('Farina', 500), ('Llet', 300), ('Sucre', 400)]
        '''
        return self._receptes[nomr]._ingredients

    def desa (self, f):
        '''
        Desa les dades en el fitxer de text de nom ⟨nomf⟩.
        '''

        if '.txt' or '.dat' not in f:
            f += '.txt'
            
        with open(f, 'w') as fe:
            productes = self.ingredients()
            receptes = self.receptes()

            for p in productes:
                fe.write(p+'\n')

            fe.write('@@'+'\n')

            for r in receptes:
                fe.write(r+'\n')

                for r_ing in self.recepta(r):
                    fe.write(r_ing[0]+' '+str(r_ing[1])+'\n')

                fe.write('@@'+'\n')

            fe.write('@@'+'\n')

    def obre(self, f):
        '''
        Recupera les dades del fitxer de text de nom ⟨nomf⟩.
        En cas que el fitxer contingui productes o receptes que ja existien,
        no les incorpora de nou i les ignora.

        '''        
        with open(f) as fe:
            receptari = fe.readlines()
            s = ''.join(receptari).split('@@')
            ll = ''.join(s)
            l = [i.split('\n') for i in s]
            del(l[-1])
            del(l[-1])

            s = []
            for i in l:
                j = []
                for k in i:
                    if k != '':
                        j.append(k)

                s.append(j)
            

            j = 0
            for i in s:
                if j == 0: # afegir productes
                    for producte in i:
                        if producte in self.ingredients():
                            pass

                        else: # aqui si k fa falta , ok PERFCTE
                            self.afegeix_producte(producte)

                else:
                    c = 0
                    for recepta in i:

                        if c == 0: # afegir recepta
                            nomr = recepta

                            if nomr in self.receptes():
                                break

                            self.afegeix_recepta(nomr)

                        else: # afegir ingredients recepta
                            r_ing = recepta.split(' ') # [producte, quantitat] no ha sigut tan llarg al final xdd ja xd
                            self.afegeix_ingredient_recepta(nomr, r_ing[0], int(r_ing[1])) #Okay, crec que ja tira, he creat una recepta que es deia pa-tom
                            #I he recuperat prova, i no m'ha modificat pa-tom. Està perfecte crec.

                        c += 1
                j += 1


if __name__ == '__main__':
    '''
    r = Receptari()
    r.recupera('prova')
    pass
    '''
