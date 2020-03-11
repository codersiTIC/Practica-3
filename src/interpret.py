#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Mòdul *interpret*
=================

Un objecte de la classe Interpret és un interpret d’ordres configurable (és
necessari configurar-lo abans d'utilitzar-lo, mitjançant la cració d'ordres i la
definició d'un prompt).

Les ordres que li configurem han d'estar relacionades amb una funció específica,
que indiqui que han de fer aquestes ordres del nostre interpret. La classe conté
els següents atributs:

prompt [str, Privat] Emmagatzema el prompt que usarà l’intèrpret.

dcom [dict, Privat] Es el diccionari que emmagatzema les ordres conegudes per l’intèrpret.
El diccionari emmagatzema una entrada per a cada ordre. Per a una ordre específica, la clau
correspon amb el nom de l’ordre i el valor és la funció que implementa l’ordre.

'''

from receptari import*
from main import *



class Interpret(object):
    """docstring for Interpret

        >>> def c1(l): print "executo l’ordre 1: {0}".format(l[0])
        >>>
        >>> def c2(l): print "executo l’ordre 2: {0}".format(l[0])
        >>>
        >>> i = Interpret()
        >>> i.set_prompt("**")
        >>>
        >>> i.afegeix_ordre("menja", c1)
        >>> i.afegeix_ordre("beu", c2)
        >>>
        >>> i.run()
        ∗∗ menja caramel
        executo l’ordre 1: caramel
        ∗∗ beu xocolata
        executo l’ordre 2: xocolata
        ∗∗ Surt
        >>>
    """
    def __init__(self):
        self._dcom = dict()
        self._prompt = str()

    def set_prompt(self,p):
        '''
        Modificador. Canvia el prompt del propi intèrpret

        :param p: El prompt que utilitzarà l'intèrpret
        :type p: str

        >>> set_prompt("**")
        >>>
        '''
        self._prompt = p

    def afegeix_ordre(self, nomc, ordre):
        '''
        Modificador. Afegeix a l’intèrpret una ordre de nom nomc associada a la funció ordre. Si
        ja existia una ordre amb aquest nom, es queixa. Noteu que el tercer paràmetre del mètode
        és una funció!
        La funció de nom ordre és una funció que té com a únic paràmetre una llista de strings.

        :param nomc: El nom associat a la funció *ordre*
        :type nomc: str
        :param ordre: Una funció qualsevol **sense ser cridada amb ()**
        :type ordre: funció

        >>> i = Interpret()
        >>> i.set_prompt("**")
        >>> def eleva2(n): return n**2
        >>>
        >>> afegeix_ordre("eleva", eleva2)
        >>>
        >>> i.run()
        ** eleva 10
        100
        ** eleva 4
        16
        ** surt
        >>>
        '''

        if self._dcom.has_key(nomc):

            return 'Failed. This command already exists'

        else:

            self._dcom[nomc] = ordre
    
    
    def run(self):
        '''
        Arrenca l’execució d’aquest intèrpret d’ordres. L’intèrpret s’executa indefinidament fins
        que l’usuari escriu l’ordre surt.
        quan tenim 3 argumnts pk estan arreve
        A cada cicle d’interpretació, l’intèrpret escriu el prompt, llegeix un string del teclat, l’ana-
        litza separant els mots que el formen. El primer mot considera que és un nom d’ordre i la
        resta de mots els paràmetres d’aquesta ordre. Finalment executa la funció corresponent a
        l’ordre i li passa com a paràmetre la resta de mots en una llista.
        '''      
        while True:
            try:
                print self._prompt,
                p = raw_input()
                ll = p.split()
                ordres = ll[1:]

                if len(ordres) == 3:
                    ordres[0], ordres[1] = ordres[1], ordres[0]
                    ordres[2] = int(ordres[2])

                if self._dcom.has_key(ll[0]):
                    if len(ordres) == 0:
                        self._dcom[ll[0]]()

                    else:
                        self._dcom[ll[0]](*ordres)

                elif ll[0] == 'surt' or ll[0] == 'Surt':
                    break

                elif ll[0] == 'help' or ll[0] == 'Help':

                    print
                    ll = self._dcom.keys()
                    ll.append('surt')
                    ll.append('help')
                    print 'Ordres disponibles:'
                    print
                    for element in sorted(ll):
                        if element == 'help':
                            print " ** help --> Menú de consulta d'ordres"

                        elif element == 'producte':
                            print ' ** producte <nom> --> Afegeix un producte al receptari de nom <nom> \n'

                        elif element == 'recepta':                            
                            print ' ** recepta <nom> --> Afegeix una recepta al receptari que té nom <nom> \n'
                            
                        elif element == 'ingredient':
                            print " ** ingredient <nomp> <nomr> <qua> --> Afegeix <qua> grams de l'ingredient de"
                            print "                                       nom <nomp> al la recepta <nomr> \n"

                        elif element == 'print':
                            print " ** print <ent> [<nom>] --> Escriu per pantalla segons el valor de <ent>. Si"
                            print "                            <ent> és: \n"
                            print "     ** receptes --> Escriu la llista de noms de receptes del receptari \n"
                            print "     ** productes --> Escriu la llista de noms de producte del receptari \n"
                            print "     ** recepta --> Escriu els ingredients i la quantitat que intervenen en la"
                            print "                    recepta de nom <nom>\n"

                        elif element == 'receptes-ing':
                            print "     ** receptes-ing --> Escriu la llista de noms de recepta en les que participa"
                            print "                         l’ingredient anomenat <nom> \n"

                        elif element == 'surt':
                            print " ** surt --> Acaba l'execució del programa"  
                    print
                    
                else:
                    print "Comanda no coneguda"

                    print

            except:
                print "Ordres i/o arguments no vàlids. Per més informació executi la comanda **help**\n"
                

