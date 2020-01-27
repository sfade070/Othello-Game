1
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: main
   :platform: Unix, Windows
   :synopsis: Main script

.. moduleauthor:: François-Xavier Dupé

"""

import othello as po
import joueur as joueur
import iafaible as iaf
import IAForte as iaF
from othello import Othello 




def lancejeu():
    """Routine de lancement du jeu"""
    print('OTHELLO avec une IA')
    
#    
    #########joueur VS joueur #######################
    jblanc = joueur.Joueur('Blanc', 'o')
    jnoir = joueur.Joueur('Noir', 'x')
    jeu = po.Othello(jblanc,jnoir)
#    ####### joueur VS ia_faible #####################
#    jblanc = joueur.Joueur('Blanc', 'o')
#    ia_faib = iaf.IAFaible('iafaible','x')
#    jeu = po.Othello(jblanc,ia_faib) 
#    ####### joueur VS ia_forte ######################
#    jblanc = joueur.Joueur('Blanc', 'o')
#    ia_fort = iaF.IAForte('iaforte','x')
#    jeu = po.Othello(jblanc,ia_fort)
#    ####### ia_faible VS ia_forte ###################
#    ia_faib = iaf.IAFaible('iafaible','o')
#    ia_fort = iaF.IAForte('iaforte','x')
#    jeu = po.Othello(ia_faib,ia_fort)
#    #################################################
#    
    jeu.info()
    jeu.jeu()

if __name__ == "__main__":
    lancejeu()
    
    
 
    
    
    
    
    
# jeu.recherche_coup_direct(jeu.plateau,jnoir, (1,0),(1,0))    
#jblanc = joueur.Joueur('Blanc', 'o')
#jnoir = iaF.IAForte('Noir_iafaible','x')
#jeu = po.Othello(jblanc, jnoir)
#Othello.Nb_transforme(jeu.plateau,jnoir,(1,0))