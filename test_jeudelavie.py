#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:55:48 2021

@author: nilsbarrellon
"""

from jeudelavie import Grille,Etat,Moteur

def testMort():
    grille=Grille(4,8)
    grille.set_case(2,2,Etat.ALIVE)
    grille.set_case(2,3,Etat.ALIVE)
    grille.set_case(3,2,Etat.ALIVE)
    grille.set_case(3,3,Etat.ALIVE)
    grille.set_case(2,4,Etat.ALIVE)
    moteur=Moteur()
    moteur.nextgen(grille)
    assert grille.get_case(2,3)==Etat.DEAD
    
def testMiseAJour():
    pass