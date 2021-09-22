#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:57:01 2021

@author: nilsbarrellon
"""
import enum


class Etat(enum.Enum):
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
        
    def update(self,grille)->None:
        assert grille.hauteur==self.hauteur and grille.largeur==self.largeur,"Tailles non homogenes"
        for i in range(grille.hauteur):
            for j in range(grille.largeur):
                self.set_case(i,j,grille.get_case(i,j))
    
    
    def nb_voisins(self,x,y,borne=8)->int:
        total_voisins = 0
        for direction in [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]:
            if self.voisin(x, y, direction):
                total_voisins += 1
                #inutile de tester toutes les cases autour si total_voisins>borne
                if total_voisins==borne:
                    return total_voisins
        return total_voisins
    
    
class Moteur:
    def __init__(self):
        pass
    
    
    def futur_etat(self, nb_voisins: int, etat: Etat) -> Etat:        
        if nb_voisins == 3:
            return Etat.ALIVE
        elif etat==Etat.ALIVE and 1< nb_voisins < 3:
            return Etat.ALIVE
        return Etat.DEAD
    
    #underscore : méthode interne inaccessible à l'exterieur
    def _futur_etat(self,x, y, grille:Grille, grilleModifiee:Grille):
        grilleModifiee.set_case(x, y,self.futur_etat(grille.nb_voisins(x, y, 4),
                                                     grille.get_case(x, y)))
    
    
    def nextgen(self, grille : Grille):
        tmp=Grille(grille.hauteur,grille.largeur)
        for x in range(grille.hauteur):
            for y in range(grille.largeur):
                self._futur_etat(x, y, grille, tmp)
        grille.update(tmp)
                