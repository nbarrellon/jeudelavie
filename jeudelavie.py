#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:57:01 2021

@author: nilsbarrellon
"""
class Etat:
    ALIVE = True
    DEAD = False
    

class Grille:
    def __init__(self, hauteur : int, largeur: int):
        self.hauteur = hauteur
        self.largeur = largeur
        self.contenu = [[Etat.DEAD for _ in range(self.largeur)] for _ in range(self.hauteur)]
        
    def set_case(self, x : int, y : int, etat : Etat):
        self.contenu[x][y] = etat
        
        
    def get_case(self, x : int, y : int):
        return self.contenu[x][y]


    def voisin(self,x, y, direction):
        delta_x, delta_y = direction
        x_new, y_new = x + delta_x, y + delta_y
        if x_new < 0 or x_new >= self.hauteur or y_new < 0 or y_new >= self.largeur:
            return Etat.DEAD
        else:
            return self.contenu[x_new][y_new]
    
    
    def nb_voisins(self,x,y,borne=8)->int:
        total_voisins = 0
        for direction in [(-1,-1), (0,-1), (1,-1), (1,0),(1,1),(0,1),(-1,1), (-1,0)]:
            if self.voisin(x, y, direction):
                total_voisins += 1
                if total_voisins==borne:
                    return total_voisins
        return total_voisins
    
    
class Moteur:
    def __init__(self):
        pass
    
    
    def futur_etat(self, nb_voisins: int, etat: Etat) -> Etat:
        return Etat.DEAD
    

    def _futur_etat(self,x, y, grille:Grille, grilleModifiee:Grille):
        if grille.get_case(x,y)==Etat.ALIVE:
            if 2 <= grille.nb_voisins(x,y,4) <= 3:
                grilleModifiee.set_case(x,y,Etat.ALIVE)
        elif grille.nb_voisins(x,y,4) == 3 :
            grilleModifiee.set_case(x,y,Etat.ALIVE) 
    
    
    def nextgen(self, grille : Grille):
        tmp=Grille(4,8)
        for x in range(grille.hauteur):
            for y in range(grille.largeur):
                self._futur_etat(x, y, grille, tmp)
        grille.contenu = tmp.contenu
                