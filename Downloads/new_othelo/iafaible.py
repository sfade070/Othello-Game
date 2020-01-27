# -*- coding: utf-8 -*-
"""
.. module:: IAFaible
   :platform: Unix, Windows
   :synopsis: Classe pour un joueur joué par une IA

.. moduleauthor:: François-Xavier Dupé

"""

#  import plateau.joueur as pj
import joueur as pj
import random


class IAFaible(pj.Joueur):
    """Classe de gestion d'une IA faible"""

    def __init__(self, nom='joueur0', pion='x'):
        """Constructeur

        :param nom: le nom du joueur
        :param pion: le type de pion pour le joueur
        """
        pj.Joueur.__init__(self, nom, pion)
        self.iatype = 'faible'

    def choix_coup(self, coups, jplateau):
        """Selection d'un coup par le joueur

        :param coups: les coups possibles pour le joueur
        :param jplateau: le plateau de jeu

        :returns: le coup choisi par le joueur (ici au hasard)
        """
        #  c=randint(0,len(coups)-1)
        c = random.randint(0, len(coups)-1)
        return coups[c]
