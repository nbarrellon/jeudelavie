#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:57:01 2021

@author: nilsbarrellon
"""
import enum, random


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
    
    
    def __str__(self) -> str:
        builder = ""
        for i in range(self.hauteur):
            builder += "|"
            for j in range(self.largeur):
                if self.get_case(i, j) == Etat.ALIVE:
                    builder+="*|"
                else:
                    builder+=" |"
            builder+="\n"
        return builder
    
    
class Moteur:
    def __init__(self, grille: Grille):
        self._grille = grille
        self._temp = Grille(grille.hauteur, grille.largeur)
    
    
    def futur_etat(self, nb_voisins: int, etat: Etat) -> Etat:        
        if nb_voisins == 3:
            return Etat.ALIVE
        elif etat==Etat.ALIVE and 1< nb_voisins < 3:
            return Etat.ALIVE
        return Etat.DEAD
    
    #underscore : méthode interne inaccessible à l'exterieur
    def _futur_etat(self,x, y):
        self._temp.set_case(x, y,self.futur_etat(self._grille.nb_voisins(x, y, 4),
                                                     self._grille.get_case(x, y)))
    
    
    def nextgen(self):
        for x in range(self._grille.hauteur):
            for y in range(self._grille.largeur):
                self._futur_etat(x, y)
        self._grille.update(self._temp)


if __name__ == "__main__":
    grille = Grille(4,8)
    for i in range(10):
        grille.set_case(random.randint(0, 3), random.randint(0, 7), Etat.ALIVE)
    moteur = Moteur(grille)
    for i in range(10):
        print(str(grille))
        moteur.nextgen()
    print(grille)
