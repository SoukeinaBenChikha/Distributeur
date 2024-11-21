# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:57:51 2023

@author: souke
"""
global nbBoisson
nbBoisson=0

class Boisson:
    """
    Description de la classe boisson.

        Attributes.
            nom (str): un nom de boisson
            prix (int): prix de boissson entier

    """
    
    def __init__(self,n=0,nm="",pr=0):
        global nbBoisson
        nbBoisson+=1
        self.num=nbBoisson
        self.nom=nm
        self.prix=pr
        
    def __str__(self):
        """Return class description."""
        s=str(self.num)+"-"+self.nom+"\t\t--------"+str(self.prix)+"\n"
        return s
    
    