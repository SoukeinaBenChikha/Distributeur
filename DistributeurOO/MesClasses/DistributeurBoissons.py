#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 11:55:10 2020

@author: soukeina
"""

import MesClasses.Menu as Menu

class Distributeur :
    def __init__(self, nom_d, lieu_d, nomF):
        self.mon_nom=nom_d
        self.mon_lieu=lieu_d
        self.mon_menu=Menu.Menu()
        self.mon_menu.creerMenuFromFile(nomF)
        self.piecesMonnaie=(5,10,20,50)
        self.dict_prix={}
        self.dict_noms={}
        for j in range(0,len(self.mon_menu.listeBoissons)):
            self.dict_prix[j]=self.mon_menu.listeBoissons[j].prix
            self.dict_noms[j]=self.mon_menu.listeBoissons[j].nom
        

    def affMenu(self):
        nombre_boissons=self.mon_menu.nbBoisson
        print("** DISTRIBUTEUR DE BOISSONS **")
        print("Faites votre choix et validez!\n")
        print(self.mon_menu)
        print("0 .  Annuler")


    def lireChoix():
        print("...")
        c=int(input())
        return c
    
    def reste_op(r):
        d_reste=dict()
        d_reste[50]=r//50
        r=r-d_reste[50]*50
        d_reste[20]=r//20
        r=r-d_reste[20]*20
        d_reste[10]=r//10
        r=r-d_reste[10]*10
        d_reste[5]=r//5
        #print(d_reste)
        dd_reste={}
        for i,j in d_reste.items():
            if(j!=0):
                dd_reste[i]=j
        #print(dd_reste)
        return dd_reste

    def run(self):
        nombre_boissons=0
        prix_boisson_choisie=0
        nom_boisson_choisie=""  
        choixClient=-1
        print("dddd")
        #Distributeur 
        while(True):      
            self.affMenu()
            choixClient=Distributeur.lireChoix()
            if(choixClient!=0):
               
                prix_boisson_choisie=self.dict_prix[choixClient]
                nom_boisson_choisie=self.dict_noms[choixClient]
                
                print("Vous avez choisi",nom_boisson_choisie,"veuillez introduire", prix_boisson_choisie,"P")
                print("Le distributeur accepte les pièces : ",self.piecesMonnaie)
                somme_piecesfornies=0
                encore=prix_boisson_choisie
                while (somme_piecesfornies<prix_boisson_choisie):
                    p=int(input("$:")) 
                    if p in self.piecesMonnaie:
                        encore-=p
                        somme_piecesfornies+=p
                        if(somme_piecesfornies<prix_boisson_choisie):
                            print("encore ",encore)
                    else:
                         print("Pièce non acceptée")
                print("Vous avez introduits",somme_piecesfornies,"P")
                print("Votre boisson est servie")
                reste=somme_piecesfornies-prix_boisson_choisie
                
                if(reste>0):
                    print("Veuillez récupérer votre reste (",reste,")...Bon appétit")
                    print("Vos pièces sont",Distributeur.reste_op(reste))
                else:
                    print("Bon appétit")
                #marche=input()
                print()
                print()
                print()
        print("FIN")




