#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:55:48 2021

@author: nilsbarrellon
"""
from jeudelavie import Grille,Etat,Moteur
import pytest


def testTailleGrille():
    grille=Grille(4,8)
    assert grille.hauteur==4,"La grille n'a pas la hauteur spécifiée lors de la construction"
    assert grille.largeur==8,'Largueur non valide'


def testGetSet():
    grille=Grille(4,8)
    grille.set_case(2,2,Etat.ALIVE)
    assert grille.get_case(2,2)==Etat.ALIVE
    grille.set_case(2, 2, Etat.DEAD)
    assert grille.get_case(2, 2)==Etat.DEAD
    grille=Grille(4,8)


def testEtatParDefaut():
    grille=Grille(4,8)
    for i in range(grille.hauteur):
        for j in range(grille.largeur):
            assert grille.get_case(i,j)==Etat.DEAD,'Case '+str((i,j))+' dans un mauvais etat'
    
            
def testFuturEtat0Dead():
    grille=Grille(0,0)
    moteur=Moteur(grille)
    moteur.nextgen()
    nb_voisin = 0
    etat = Etat.DEAD
    etat_retour = Etat.DEAD
    assert etat_retour == moteur.futur_etat(nb_voisin, etat)
    
 
def testFuturEtat0Alive():
    grille=Grille(0,0)
    moteur=Moteur(grille)
    moteur.nextgen()
    nb_voisin = 0
    etat = Etat.ALIVE
    etat_retour = Etat.DEAD
    assert etat_retour == moteur.futur_etat(nb_voisin, etat)
    
 
def testFuturEtat1Dead():
    grille=Grille(0,0)
    moteur=Moteur(grille)
    moteur.nextgen()
    nb_voisin = 1
    etat = Etat.DEAD
    etat_retour = Etat.DEAD
    assert etat_retour == moteur.futur_etat(nb_voisin, etat)
    
 
def testFuturEtat1Alive():
    grille=Grille(0,0)
    moteur=Moteur(grille)
    moteur.nextgen()
    nb_voisin = 1
    etat = Etat.ALIVE
    etat_retour = Etat.DEAD
    assert etat_retour == moteur.futur_etat(nb_voisin, etat)
    
 
def testFuturEtat2Alive():
    grille=Grille(0,0)
    moteur=Moteur(grille)
    moteur.nextgen()
    nb_voisin = 2
    etat = Etat.ALIVE
    etat_retour = Etat.ALIVE
    assert etat_retour == moteur.futur_etat(nb_voisin, etat)
    
 
def testFuturEtat2Dead():
    grille=Grille(0,0)
    moteur=Moteur(grille)
    moteur.nextgen()
    nb_voisin = 2
    etat = Etat.DEAD
    etat_retour = Etat.DEAD
    assert etat_retour == moteur.futur_etat(nb_voisin, etat)
    
 
def testFuturEtat3Dead():
    grille=Grille(0,0)
    moteur=Moteur(grille)
    moteur.nextgen()
    nb_voisin = 3
    etat = Etat.DEAD
    etat_retour = Etat.ALIVE
    assert etat_retour == moteur.futur_etat(nb_voisin, etat)
    
 
def testFuturEtat3Alive():
    grille=Grille(0,0)
    moteur=Moteur(grille)
    moteur.nextgen()
    nb_voisin = 3
    etat = Etat.ALIVE
    etat_retour = Etat.ALIVE
    assert etat_retour == moteur.futur_etat(nb_voisin, etat)
    
 
def testFuturEtat4plusDead():
    grille=Grille(0,0)
    moteur=Moteur(grille)
    moteur.nextgen()
    for nb_voisin in range(4,9):
        etat = Etat.DEAD
        etat_retour = Etat.ALIVE
        assert etat_retour == moteur.futur_etat(nb_voisin, etat)
    
 
def testFuturEtat4plusAlive():
    grille=Grille(0,0)
    moteur=Moteur(grille)
    moteur.nextgen()
    for nb_voisin in range(4,9):
        etat = Etat.ALIVE
        etat_retour = Etat.DEAD
        assert etat_retour == moteur.futur_etat(nb_voisin, etat)
        
        
def testCopieGrille():
    grille=Grille(4,4)
    grilleCopie=Grille(4,4)
    grilleCopie.set_case(2,2,Etat.ALIVE)
    
    grille.update(grilleCopie)
    
    assert grille.get_case(2,2)==Etat.ALIVE
    
    
def testCopieGrille2():
    grille=Grille(4,4)
    grilleCopie=Grille(2,2)
    with pytest.raises(AssertionError):
        grille.update(grilleCopie)
 
    
def testMort():
    grille=Grille(4,8)
    grille.set_case(2,2,Etat.ALIVE)
    grille.set_case(2,3,Etat.ALIVE)
    grille.set_case(3,2,Etat.ALIVE)
    grille.set_case(3,3,Etat.ALIVE)
    grille.set_case(2,4,Etat.ALIVE)
    moteur=Moteur(grille)
    moteur.nextgen()
    assert grille.get_case(2,3)==Etat.DEAD
    
    
def testMort2():
    grille=Grille(12,12)
    grille.set_case(2,2,Etat.ALIVE)
    grille.set_case(2,3,Etat.ALIVE)
    grille.set_case(3,2,Etat.ALIVE)
    grille.set_case(3,3,Etat.ALIVE)
    grille.set_case(2,4,Etat.ALIVE)
    moteur=Moteur(grille)
    moteur.nextgen()
    assert grille.get_case(2,3)==Etat.DEAD
    
    
def testNbVoisins():
    grille=Grille(4,8)
    grille.set_case(0,3,Etat.ALIVE)
    grille.set_case(1,0,Etat.ALIVE)
    grille.set_case(1,6,Etat.ALIVE)
    grille.set_case(1,7,Etat.ALIVE)
    grille.set_case(2,0,Etat.ALIVE)
    grille.set_case(2,6,Etat.ALIVE)
    grille.set_case(2,7,Etat.ALIVE)
    grille.set_case(3,0,Etat.ALIVE)
    grille.set_case(3,1,Etat.ALIVE)
    
    assert grille.nb_voisins(2, 1) == 4, "Le nombre de voisins devrait etre detecte"


def testMiseAJour():
    grille=Grille(4,8)
    grille.set_case(0,3,Etat.ALIVE)
    grille.set_case(1,0,Etat.ALIVE)
    grille.set_case(1,6,Etat.ALIVE)
    grille.set_case(1,7,Etat.ALIVE)
    grille.set_case(2,0,Etat.ALIVE)
    grille.set_case(2,6,Etat.ALIVE)
    grille.set_case(2,7,Etat.ALIVE)
    grille.set_case(3,0,Etat.ALIVE)
    grille.set_case(3,1,Etat.ALIVE)
    moteur=Moteur(grille)
    moteur.nextgen()
    assert grille.get_case(0,3)==Etat.DEAD
    assert grille.get_case(1,0)==Etat.DEAD
    assert grille.get_case(0,3)==Etat.DEAD
    assert grille.get_case(2,1)==Etat.ALIVE
    assert grille.get_case(1,6)==Etat.ALIVE
    assert grille.get_case(1,7)==Etat.ALIVE
    assert grille.get_case(2,6)==Etat.ALIVE
    assert grille.get_case(2,7)==Etat.ALIVE
