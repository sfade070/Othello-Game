# -*- coding: utf-8 -*-
"""
.. module:: joueur
   :platform: Unix, Windows
   :synopsis: Classe principale pour un joueur

.. moduleauthor:: François-Xavier Dupé

"""


class Joueur(object):
    """Classe de gestion d'un joueur"""

    def __init__(self, nom='Toto', pion='x'):
        """Constructeur

        :param nom: le nom du joueur
        :param poin: le type de pion du joueur
        """
        self.nom = nom
        self.pion = pion

    def choix_coup(self, coups, jplateau):
        """Selection d'un coup par le joueur

        :param coups: les coups possibles

        :returns: le coup choisi par le joueur
        """
        print(self.nom, '(', self.pion, ')', ' a vous de jouer')
        if len(coups) is 0:
            print('Pas de coup a jouer')
            return []
        else:
            print('voici vos coups')
            for i in range(len(coups)):
                print(i, ') => ', coups[i])
            rep = 0
            while True:
                try:
                    rep = input('Choix du coup : ')
                    rep = int(rep)
                    if rep >= len(coups):
                        continue
                    break
                except Exception as e:
                    print('Entree invalide')

            return coups[rep]

    def info(self):
        """Affiche des infos sur le joueur"""
        print('Joueur = ', self.nom)
        print('Pion = ', self.pion)
