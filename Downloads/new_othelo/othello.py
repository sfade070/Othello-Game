# -*- coding: utf-8 -*-
"""
.. module:: othello
   :platform: Unix, Windows
   :synopsis: Main class for the Othello game

.. moduleauthor:: François-Xavier Dupé

"""
#import plateau.joueur


class Othello(object):
    """Classe pour le jeu"""

    def __init__(self, jblanc, jnoir):
        """Constructeur"""
        self.plateau = []
        self.ecoute_coup = []
        #self.jnoir = plateau.joueur.Joueur('Noir', 'x')
        self.jnoir = jnoir
       # self.jblanc = plateau.iafaible.IAFaible('Blanc', 'o')
        self.jblanc = jblanc
        self.faire_plateau()

    def faire_plateau(self):
        """Construction du plateau de jeu"""
        # Construction des cases
        self.plateau=[]
        for i in range(0,8):
            ligne=[" "]*8
            self.plateau.append(ligne)
            
        self.plateau[3][3]=self.jblanc.pion
        self.plateau[3][4]=self.jnoir.pion 
        self.plateau[4][3]=self.jnoir.pion     
        self.plateau[4][4]=self.jblanc.pion      
        
       

    def jeu(self):
        """Routine de lancement d'une partie"""
        
        print('Lancement du Jeu')
        while True:
            # Alternance des joueurs
            self.info()
            print(self.calcul_score())
            depl = 0
            res = self.tour_joueur(self.jnoir)
            depl += res
            self.info()
            res = self.tour_joueur(self.jblanc)
            depl += res
            if depl is 0:
                break
        score = self.calcul_score()
        if score['x'] > score['o']:
            print('Joueur ', self.jnoir.nom, ' a gagner')
        elif score['x'] < score['o']:
            print('Joueur', self.jblanc.nom, 'a gagner')
        else:
            print('Egalite donc pas de vainqueur')

    def tour_joueur(self, joueur):
        """Tour d'un joueur

            :param joueur: le joueur dont c'est le tour

            :returns: 0 si aucun coup n'est joué, 1 sinon
        """
        proch_coups = self.prochain_coups(self.plateau, joueur)
        if proch_coups:
            chx_coup = joueur.choix_coup(proch_coups, self.plateau)
            Othello.jouer_coup(self.plateau, joueur, chx_coup)
            return 1
        return 0


    @staticmethod
    def jouer_coup(jplateau, joueur, coup):
        """Le joueur joue un coup

        :param jplateau: le plateau de jeu
        :param joueur: le joueur dont c'est le tour
        :param coup: le coup à jouer
        """
        jplateau[coup[0]][coup[1]] = joueur.pion
        Othello.propager_coup(jplateau, joueur, coup)
        
    

    def info(self):
        """Donne des informations sur le jeu"""
        print('Jeu Othello')
        print('x / y 0    1    2    3    4    5    6    7')
        for i in range(8):
            print(i, ' ', self.plateau[i])
        
        
                
        
        

    @staticmethod
    def limite(pos):
        """Test si une position est dans le plateau

        :param pos: la position
        :returns: True si OK, False sinon
        """
        x=pos[0] 
        y=pos[1]
        if x>=0 and x < 8  and y>=0 and y < 8:  
            return True  
        else:
            return False     

  



    @staticmethod
    def prochain_coups(jplateau, joueur):
        """Calcul des prochains coups possibles

        :param jplateau: le plateau de jeu
        :param joueur: le joueur courant

        :returns: la liste de coups que le joueur peut jouer
        """
        
        coups=[]  
        for i in  range(8): 
           for j in range (8): 
              if jplateau[i][j] == ' ' and  Othello.recherche_coup(jplateau, joueur, (i,j)) : 
                coups.append((i,j))     
        return coups     
        
    

    @staticmethod
    def recherche_coup_direct(jplateau, joueur, pos, direc):
        """Recherche si un coup est possible le long d'une direction

        :param jplateau: le plateau de jeu
        :param joueur: le joueur courant (le pion)
        :param pos: la position de départ
        :param direc: la direction à regarder (ici une fonction de déplacement)

        :returns: True si le coup est possible, False sinon
        """
        x=pos[0]+direc[0]
        y=pos[1]+direc[1]
        vuadversaire=False
      
        while Othello.limite([x,y]) and jplateau[x][y] != joueur.pion and jplateau[x][y] != ' '  :
            vuadversaire=True 
            (x,y)= (x+direc[0], y+direc[1]) 
        if Othello.limite([x,y]) and jplateau[x][y] == joueur.pion: 
            return vuadversaire
            
        return False     




    @staticmethod
    def recherche_coup(jplateau, joueur, pos):
        """Recherche du prochain a partir de la position et du joueur

        :param jplateau: le plateau de jeu
        :param joueur: le joueur
        :param pos: la position du coup

        :returns: True si le coup est possible, False sinon
        """
        direc=[(-1,1),(-1,-1),(0,1),(0,-1),(1,-1),(1,0),(1,1),(0,1)] 
        for d in direc : 
               if Othello.recherche_coup_direct(jplateau, joueur, pos,d):
                   return True 
        return False 

        
    
    @staticmethod
    def propager_coup(jplateau, joueur, coup):
        """Propagation d'un coup

        :param jplateau: le plateau de jeu
        :param joueur: le joueur
        :param coup: le coup joué par le joueur
        """
        for i in range(-1,2):
            for j in range(-1,2):  #tester toutes les directions
                if [i,j]!=[0,0] and Othello.recherche_coup_direct(jplateau, joueur, coup, [i,j]): # si les condition sont verifier je change la position
                    position = (coup[0] +i, coup[1] +j) 
                    while jplateau[position[0]][position[1]]!=joueur.pion: #tant que je croise pas mon pion j'avance
                        jplateau[position[0]][position[1]] = joueur.pion
                        position = (position[0] +i, position[1] +j) 

        
    

    def calcul_score(self):
        """Calcul le score des joueurs

        :returns: le score (nombre de pions) de chaque joueur
        """
        score = {'x': 0, 'o': 0}
        for i in range(8):
            for j in range(8):
                if self.plateau[i][j] == 'x':
                    score['x'] = score['x'] + 1
                elif self.plateau[i][j] == 'o':
                    score['o'] += 1
        return score
    
    
    
    @staticmethod
    def Nb_transforme(jplateau,joueur,coup):
        """Prend en entrée un plateau de jeu, un joueur et le coup joué par le joueur 

        :returns: le nombre de transformation possible pour un coup donné. 
        """
        c=0
        for i in range(-1,2):
            for j in range(-1,2): 
                if [i,j]!=[0,0] and Othello.recherche_coup_direct(jplateau, joueur, coup, [i,j]): 
                    position = (coup[0] +i, coup[1] +j)
                    
                    while jplateau[position[0]][position[1]]!=joueur.pion:
                        position = (position[0] +i, position[1] +j)
                        c=c+1
                        
       
        return c