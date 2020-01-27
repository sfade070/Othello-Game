# -*- coding: utf-8 -*-
"""
.. module:: IAforte
   :platform: Unix, Windows
   :synopsis: Classe pour un joueur joué par une IA

.. moduleauthor:: François-Xavier Dupé

"""

#  import plateau.joueur as pj
import joueur as pj
import random
from othello import Othello
import numpy


class IAForte(pj.Joueur):
    """Classe de gestion d'une IA faible"""

    def __init__(self, nom='joueur0', pion='x'):
        """Constructeur

        :param nom: le nom du joueur
        :param pion: le type de pion pour le joueur
        """
        pj.Joueur.__init__(self, nom, pion)
        self.iatype = 'Forte'


 
        
    def choix_coup(self, coups, jplateau):
        """Selection d'un coup par le joueur

        :param coups: les coups possibles pour le joueur
        :param jplateau: le plateau de jeu

        :returns: le coup choisi par le joueur (ici prend le coup qui a le plus grand nombre de point a gagné,)
        """
        
        C=[Othello.Nb_transforme(jplateau,self,coup) for coup in coups]
        c=numpy.argmax(C)

        return coups[c] 


            
        
