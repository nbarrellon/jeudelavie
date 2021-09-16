#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:57:01 2021

@author: nilsbarrellon
"""

class Etat:
    ALIVE = True
    DEAD = False
    
    def __init__(self):
        return

class Grille:
    def __init__(self, hauteur : int, largeur: int):
        self.hauteur = hauteur
        self.largeur = largeur
        self.contenu = [[Etat.DEAD for _ in range(self.largeur)] for _ in range(self.hauteur)]
        
    def set_case(self, x : int, y : int, etat : Etat):
        self.contenu[x][y] = etat
        
    def get_case(self, x : int, y : int):
        return self.contenu[x][y]

def voisin(x, y, direction, depart):
    hauteur, largeur = len(depart), len(depart[0])
    delta_x, delta_y = direction
    x_new, y_new = x + delta_x, y + delta_y
    if x_new < 0 or x_new >= hauteur or y_new < 0 or y_new >= largeur:
        return Etat.DEAD
    else:
        return depart[x_new][y_new]

def nb_voisins(x, y, depart):
    total_voisins = 0
    for direction in [(-1,-1), (0,-1), (1,-1), (1,0),(1,1),(0,1),(-1,1), (-1,0)]:
        if voisin(x, y, direction, depart):
            total_voisins += 1
    return total_voisins
    

def futur_etat(x, y, depart, destination):
    if depart[x][y]:
        if 2 <= nb_voisins(x, y, depart) <= 3:
            destination[x][y] = Etat.ALIVE
        else:
            destination[x][y] = Etat.DEAD
    else:
        destination[x][y] = Etat.ALIVE if nb_voisins(x, y, depart) == 3 else Etat.DEAD
    
class Moteur:
    def __init__(self):
        pass
    
    def nextgen(self, grille : Grille):
        tmp = [[elm for elm in ligne] for ligne in grille.contenu]
        for x in range(grille.hauteur):
            for y in range(grille.largeur):
                futur_etat(x, y, grille.contenu, tmp)
        grille.contenu = tmp
                