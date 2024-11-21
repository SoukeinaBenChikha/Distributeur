# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:50:23 2023

@author: souke
"""

import MesClasses.DistributeurBoissons as dist

def main():
    monDistributeur = dist.Distributeur("M2i","Aix-en-Provence", "Data/menu.txt")
    monDistributeur.run()


if __name__ =='__main__':
    main()


