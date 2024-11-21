# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:47:38 2023

@author: souke
"""
import MesClasses.Boisson 
import sys

class Menu:
    def __init__(self):
        self.nbBoisson=0
        self.listeBoissons=[]
        
    def __addBoisson__(self, boiss):
        self.listeBoissons.append(boiss)
        self.nbBoisson+=1
    
    def __chargerDonnees__(self, nomFichier):
        try:
            F=open(nomFichier,"r")
            lignes= F.readlines()
            F.close()
            return lignes
        except FileNotFoundError as e:
            print("probleme Ouverture menu ",e)
            sys.exit(-1)
            
    
    def creerMenuFromFile(self,nomFichier):
        data =self. __chargerDonnees__(nomFichier)
        j=1
        nombre_boissons=len(data)
        #print(nombre_boissons)
        for i in data:
            p_sep=i.index('-')
            nom_b=i[0:p_sep]
            prix_b=int(i[p_sep+1:])
            
            uneBoissson=MesClasses.Boisson.Boisson(j,nom_b,prix_b)
            j+=1
            self.__addBoisson__(uneBoissson)
            
        
    def __str__(self):
        s=""
        for i in self.listeBoissons:
            s+=str(i)
        return s





