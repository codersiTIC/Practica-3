#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Mòdul *main*
============

El modul main.py conte el programa principal.
Aquest programa crea una instància de Receptari
i una instància d’Interpret juntament amb les
funcions que implementen les ordres necessaries.

A continuació, engega l’intèrpret. Aquest es va
comunicant interactivament amb l’usuari fins acabar
la sessió.

L’interpret ha de tenir les seguents ordres:

producte <nom> -- Receptari.afegeix_producte(nomp)
    Afegeix un producte al receptari que te nom <nom>.

recepta <nom> -- Receptari.afegeix_recepta(n)
    Afegeix una recepta al receptari que te nom <nom>.

ingredient <nomp> <nomr> <qua> -- Receptari.afegeix_ingredient_recepta(nomr,nomp,q)
    Afegeix <qua> grams de l’ingredient de nom <nomp> a la recepta de nom <nomr>.


print <ent> [<nom>]
    Escriu per pantalla segons el valor de <ent>. Si <ent> és:

    receptes
        Escriu la llista de noms de receptes del receptari.
    productes
        Escriu la llista de noms de producte del receptari.

    recepta
        Escriu els ingredients i la quantitat que intervenen en la recepta de nom <nom>.

    receptes-ing
        Escriu la llista de noms de recepta en les que participa l’ingredient anomenat <nom>.

    surt
    Acaba l’execució del programa.
'''

from receptari import*
from interpret import*


def printlist(ent = str(), nom = str()):
    if ent == 'receptes':
        print r.receptes()

    elif ent == 'productes':
            print r.ingredients()

    elif ent == 'recepta':
        if nom in r.receptes():
            print r.recepta(nom)
        else:
            print ("La recepta < %s > no existeix")%(nom)

    elif ent == 'receptes-ing':
        if nom in r.ingredients():
            print r.receptes_ingredient(nom)
        else:
            print ("El producte < %s > no existeix")%(nom)

    else:
        print "Ordres i/o arguments no vàlids. Per més informació executi la comanda **help**"

if __name__ == '__main__':

    r = Receptari()
    i = Interpret()
    i.set_prompt('**')

    i.afegeix_ordre('producte', r.afegeix_producte)
    i.afegeix_ordre('receptes', r.receptes)
    i.afegeix_ordre('recepta', r.afegeix_recepta)
    i.afegeix_ordre('ingredient', r.afegeix_ingredient_recepta)
    i.afegeix_ordre('print', printlist)
    i.afegeix_ordre('desa', r.desa)
    i.afegeix_ordre('recupera', r.recupera)

    print "Recorda consultar el menu d'ajuda amb la comanda **help** per qualsevol dubte"
    print
    i.run()

