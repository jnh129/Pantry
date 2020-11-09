# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 08:33:25 2020

@author: Jonah
"""

import os, sys, warnings

warnings.filterwarnings("ignore")

mypath = os.path.dirname(__file__)
sys.path.append(mypath)

from PantryObject import Pantry

def main():
    choice = input("Welcome to Pantry.py! Would you like to create a new database or access an already existing one? ")
    if choice.lower() in "create a new one":
        print()
        create = input("What would you like to call this database? ")
        if os.path.exists(f'{create}.csv'):
            print(f"\n {create} already exists. \n")
            main()
    else:
        create = input("What database would you like to open? ")
        if not os.path.exists(f'{create}.csv'):
            print(f"\n {create} does not exist. \n")
            main()
    pantry = Pantry(name = create, loc = mypath)
    first_choice = input("Select what you would like to do or say quit to end: \n 1. Add items \n 2. Check inventory \n 3. Change inventory \n")
    while first_choice.lower() not in ["quit", "q"]:
        if first_choice.lower() not in ["quit", "q", "1", "2", "3", "4"]:
            print()
            print("Invalid input. \n")
        elif int(first_choice) == 1:
            print()
            pantry.add_items()
        elif int(first_choice) == 2:
            print()
            pantry.check_inventory()
        elif int(first_choice) == 3:
            print()
            pantry.update_inventory()
        first_choice = input("Select what you would like to do or say quit to end: \n 1. Add items \n 2. Check inventory \n 3. Change inventory \n" )
    print()
    print("Have a nice day!")
    
if __name__ == "__main__":
    main()

