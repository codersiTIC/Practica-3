#!/usr/bin/env python -*- coding: utf-8 -*-

''' Mòdul *main* ============

El modul main.py conte el programa principal. Aquest programa crea una instància
de Receptari i una instància d’Interpret juntament amb les funcions que
implementen les ordres necessaries.

A continuació, engega l’intèrpret. Aquest es va comunicant interactivament amb
l’usuari fins acabar la sessió.

L’interpret ha de tenir les seguents ordres:

producte <nom> -- Receptari.afegeix_producte(nomp) Afegeix un producte al
    receptari que te nom <nom>.

recepta <nom> -- Receptari.afegeix_recepta(n) Afegeix una recepta al receptari
    que te nom <nom>.

ingredient <nomp> <nomr> <qua> --
    Receptari.afegeix_ingredient_recepta(nomr,nomp,q) Afegeix <qua> grams de
    l’ingredient de nom <nomp> a la recepta de nom <nomr>.


print <ent> [<nom>] Escriu per pantalla segons el valor de <ent>. Si <ent> és:

    receptes Escriu la llista de noms de receptes del receptari. productes
        Escriu la llista de noms de producte del receptari.

    recepta Escriu els ingredients i la quantitat que intervenen en la recepta
        de nom <nom>.

    receptes-ing Escriu la llista de noms de recepta en les que participa
        l’ingredient anomenat <nom>.

    surt Acaba l’execució del programa. '''

from receptari import* from interpret import*


def help(): print print 'Ordres disponibles:' print print ' ** producte <nom>
    --> Afegeix un producte al receptari de nom <nom> \n' print ' ** recepta
    <nom> --> Afegeix una recepta al receptari que té nom <nom> \n' print " **
    ingredient <nomp> <nomr> <qua> --> Afegeix <qua> grams de l'ingredient de"
    print " nom <nomp> al la recepta <nomr> \n" print " ** print <ent> [<nom>]
    --> Escriu per pantalla segons el valor de <ent>. Si" print " <ent> és: \n"
    print " ** receptes --> Escriu la llista de noms de receptes del receptari
    \n" print " ** productes --> Escriu la llista de noms de producte del
    receptari \n" print " ** recepta --> Escriu els ingredients i la quantitat
    que intervenen en la" print " recepta de nom <nom>\n" print " **
    receptes-ing --> Escriu la llista de noms de recepta en les que participa"
    print " l’ingredient anomenat <nom> \n" print " ** surt --> Acaba l'execució
    del programa"


def printlist(ent = str(), nom = str()): if ent == 'receptes': for i in
    r.receptes(): print i

    elif ent == 'productes': for i in r.ingredients(): print i

    elif ent == 'recepta': if nom in r.receptes(): for i in r.recepta(nom):
        print str(i[1])+'gr', i[0] else: print ("La recepta < %s > no
        existeix")%(nom)

    elif ent == 'receptes-ing': if nom in r.ingredients(): for i in
        r.receptes_ingredient(nom): print i else: print ("El producte < %s > no
        existeix")%(nom)

    else: print "Ordres i/o arguments no vàlids. Per més informació executi la
        comanda **help**"

if __name__ == '__main__':

    r = Receptari() i = Interpret() i.set_prompt('**')

    i.afegeix_ordre('producte', r.afegeix_producte) i.afegeix_ordre('receptes',
    r.receptes) i.afegeix_ordre('recepta', r.afegeix_recepta)
    i.afegeix_ordre('ingredient', r.afegeix_ingredient_recepta)
    i.afegeix_ordre('print', printlist) i.afegeix_ordre('help', help)

    print "Recorda consultar el menu d'ajuda amb la comanda **help** per
    qualsevol dubte" print i.run()
