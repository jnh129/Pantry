#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''pantry.py is the personal pantry manager. You can add/remove or update items, and use it to search for an item 
   on Amazon. If an item is low, it will prompt an Amazon search. '''



import webbrowser as wb
import pandas as pd
import os.path
import os
import csv
from IPython.core.display import HTML


# In[ ]:


# wb.open('https://www.google.com')

def check_file(): # checks for pantry.csv
    
    # if true, imports dataframe
    if os.path.exists("pantry.csv"):
        
        pantry = pd.read_csv(r'pantry.csv') # reads from pantry.csv
        print("pantry.csv located successfully. Imported data.")
    
    # if false, creates dataframe and new file
    else: 
        
        with open('pantry.csv', 'wb') as csvfile: # creates pantry.csv
                  filewriter = csv.writer(csvfile, delimiter=',',
                  quotechar='|', quoting=csv.QUOTE_MINIMAL)
                
        pantry = pd.DataFrame(columns = ["Item", "Quantity", "Link"]) # creates table
        pantry.to_csv(r'pantry.csv', index = False) # writes to pantry.csv
        print("pantry.csv could not be located. Created new file.")
        
    return pantry


# In[ ]:


def make_link(phrase): # creates Amazon search link
    phrase = phrase.replace(" ","+")
    phrase = phrase.replace("-","+")
    link = "https://www.amazon.com/s?k="+phrase+"&ref=nb_sb_noss_2"
    return link

def add_items(target):
    
    new_item, quantity = input("Enter the item or say quit to end: "), 0
    
    while new_item.lower() not in ["quit", "q"]:
        if new_item not in ["quit", "Quit", "Q"]:
            while True:
                try:
                    quantity = int(input("Enter the quantity: "))
                    break
                except ValueError:
                    print("Please enter a number.\n")
            new_row = {"Item": new_item , "Quantity": quantity, "Link": make_link(new_item)}
            target = target.append(new_row, ignore_index = True)
        new_item = input("Enter the item or say quit to end: ")
            
    target.to_csv(r'pantry.csv', index = False)
    print()
    print("first_aid.csv updated successfully.")
    return target


# In[ ]:


def check_inventory(target):
    disp_col = set(target.columns)
    disp_col.remove('Link')
    display(HTML(target[disp_col].to_html()))
    lows = []
    for row in target.iterrows(): 
        if row[1]['Quantity'] == 0:
            lows.append(row)
    if len(lows) == 0:
        print("Looks all good!")
    else:
        print("The following are low:\n")
        for row in lows:
            print(str(row[0])+".", row[1]['Item']+",", "Quantity: "+str(row[1]['Quantity']))
            print()
    selection = input("Would you like to order one of these? ")
    if selection in ["Y", "y", "Yes", "yes"]:
        choice = input("Type the index of the item you would like to purchase: ")
        wb.open(target['Link'][int(choice)])
        
            
    
    


# In[ ]:


def update_inventory(target):
    disp_col = set(target.columns)
    disp_col.remove('Link')
    display(HTML(target[disp_col].to_html()))
    first_choice = input("Which item would you like to update? Say quit to exit. ")
    while first_choice not in ["quit", "Quit", "q", "Q"]:
        if int(first_choice) < 0 or int(first_choice) > len(target):
            print("Invalid input.")
            print()
        else:
            display(HTML(target[['Item','Quantity']][int(first_choice):(int(first_choice)+1)].to_html()))
            print()
            p_m = input("Would you like to add or subtract to this? ")
            if p_m.lower() == "add":
                print()
                dx = int(input("Enter how much you would like to add: ")) 
                target['Quantity'][int(first_choice)] += dx
            elif p_m.lower() == "subtract":
                print()
                dx = int(input("Enter how much you would like to add: "))
                target['Quantity'][int(first_choice)] -= dx
                
            target.to_csv(r'pantry.csv',index = False)
            print()
            second_choice = input("Your pantry has been updated. Would you like to change anything else? ")
            if second_choice.lower() in ["n","no"]:
                first_choice = "quit"
            elif second_choice.lower() in ["y","yes"]:
                first_choice = input("Which item would you like to update? ")
    return target
    
            


# In[ ]:


# Need to work on this. Messing up data table and/or crashing on repeated df.reset_index()

'''

def remove_item(target):
    disp_col = set(target.columns)
    disp_col.remove('Link')
    display(HTML(target[disp_col].to_html()))
    print()
    selection = input("Select the index of the item you would like to remove or say quit: ")
    while selection.lower() not in ["q", "quit"]:
        if selection not in [str(i) for i in range(len(target))]:
            print()
            print("Invalid input.\n")
            selection = input("Select the index of the item you would like to remove or say quit: ")
        else:
            target = target.drop(int(selection)).reset_index(drop = True)
            print()
            selection_2 = input("Would you like to remove anything else? ")
            if selection_2.lower() in ["n", "no"]:
                selection = "q"
            elif selection_2.lower() not in ["y", "yes", "n", "no"]:
                print()
                print("Invalid selection")
                selection = "q"
            else:
                disp_col = set(target.columns)
                disp_col.remove('Link')
                display(HTML(target[disp_col].to_html()))
                selection = input("Select the index of the item you would like to remove or say quit: ")
    target.to_csv(r"pantry.csv")
    return target
            
'''
    


# In[ ]:


if __name__ == "__main__":
    pantry = check_file()
    first_choice = input("Greetings. I am py-pantry, your pantry manager! Select what you would like to do or say quit to end: \n 1. Add items \n 2. Check inventory \n 3. Change inventory \n")
    while first_choice not in ["quit", "Quit", "q", "Q"]:
        if first_choice not in ["quit", "Quit", "q", "Q", "1", "2", "3", "4"]:
            print()
            print("Invalid input. \n")
        elif int(first_choice) == 1:
            print()
            pantry = add_items(pantry)
        elif int(first_choice) == 2:
            print()
            check_inventory(pantry)
        elif int(first_choice) == 3:
            print()
            pantry = update_inventory(pantry)
        first_choice = input("Select what you would like to do or say quit to end: \n 1. Add items \n 2. Check inventory \n 3. Change inventory \n" )
    print()
    print("Have a nice day!")
        
        


# 

# In[ ]:





# In[ ]:


# For my own use. Clears data from pantry dataframe and pantry.csv
'''
def clear(df, target_file):
    os.remove(target_file)
    df = pd.DataFrame(None)
    print("Cleared pantry df and pantry.csv.")
    return df

pantry = clear(pantry, "pantry.csv")
'''


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




