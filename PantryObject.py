# -*- coding: utf-8 -*-
"""
Object-oriented version of Pantry.py
"""

import pandas as pd, os, csv, os.path, webbrowser as wb

class Pantry:
    ''' Pantry object ''' 
    
    def __init__(self, name, loc):
        self.file = fr'{name}.csv'
        self.name = name
        self.location = fr'{loc}\{self.file}'
        if os.path.exists(self.location):
            self.df = pd.read_csv(self.location)
            print(f'{self.file} located and imported.')
        else:
            with open(self.file, 'wb') as csvfile:
                
                self.df = pd.DataFrame({'Item':[], 'Quantity':[], 'Link':[]})
                self.df.to_csv(self.location, index = False)
            print(f'Could not locate {self.file}. Created new file.')
    def __str__(self):
        return "Hi, I am your personal pantry management system! :)"

    def add_items(self):
        ''' Adds items to self.df'''
        new_item, quantity = input("Enter a new item or say quit to end: "), 0
        while new_item.lower() not in ['quit', 'q']:
            while True:
                try:
                    quantity = int(input("Enter the quantity: "))
                    break
                except ValueError:
                    print("Please enter a number.\n")
            phrase = new_item.replace(" ", "+")
            phrase = phrase.replace("-","+")
            link = fr"https://www.amazon.com/s?k={phrase}&ref=nb_sb_noss_2"
            new_row = {'Item':new_item, 'Quantity':quantity,'Link':link}
            self.df = self.df.append(new_row, ignore_index = True)
            new_item,quantity = input("Enter a new item or say quit to end: "), 0
        self.df.to_csv(self.location, index = False)
    
    def check_inventory(self):
        '''Print dataframe and prompt Amazon order'''
        disp_col = set(self.df.columns)
        disp_col.remove('Link')
        print(self.df[disp_col])
        lows = []
        for row in self.df.iterrows():
            if row[1]['Quantity'] == 0:
                lows.append(row)
        if len(lows) == 0:
            print("\n Everything looks good!\n")
        else:
            print("\n The following are running low: \n")
            for row in lows:
                print(str(row[0])+".", row[1]["Item"]+",","Quantity: "+str(row[1]["Quantity"])+"\n")
        selection = input("Would you like to order anything? ")
        if selection.lower() in ['y','yes']:
            choice = input("Type the index of the item you would like to purchase: ")
            wb.open(self.df['Link'][int(choice)])
        
    def update_inventory(self):
        '''Update quantities'''
        disp_col = set(self.df.columns)
        disp_col.remove('Link')
        print(self.df[disp_col])
        first_choice = input("Which item would you like to update? Say quit to exit: ")
        while first_choice.lower() not in ['q','quit']:
            if int(first_choice) < 0 or int(first_choice) > len(self.df):
                print("Invalid.\n")
            else:
                print(self.df[disp_col].iloc[int(first_choice)])
                print()
                p_m = input("Would you like to add or subtract to this? ")
                if p_m.lower() == "add":
                    dx = int(input("Enter how much you would like to add: "))
                    self.df['Quantity'][int(first_choice)] += dx
                elif p_m.lower() == "subtract":
                    dx = int(input("Enter how much you would like to subtract: "))
                    self.df['Quantity'][int(first_choice)] -= dx
                self.df.to_csv(self.location, index = False)
            first_choice = input("Which item would you like to update? Say quit to exit: ")
                
                
                
                
        
        