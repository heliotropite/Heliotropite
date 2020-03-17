# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:32:30 2020

@author: Eileen
"""
strChoice = ''
dicRow = {}
strFileName = 'CDInventory.txt'
objFile = None

class CDInventory():
    def __init__(self, strFileName):
        self.table = []
        self.filename = strFileName #'CDInventory.txt'
            
    def __repr__(self):
        return 'This is a list of dictionaries, each of which hold the details of a single CD album.'
    
    def read_file(self, filepath = self.filename):
        objFile = open(self.filepath, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            self.table.append(dicRow)
        objFile.close()
    
    def write_file(self):
        objFile = open(self.filename, 'w')
        for row in self:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        
    def add_album(self, choice):
        if choice == 'y':
            count = 1
            for row in self:
                if row['ID'] == count:
                    count += 1
                else:
                    ID = count
                    break
        else:
            ID = int(input('Please input the ID number for this album.\n'))
        album = input('Please input the album name.\n')
        artist = input('Please input the artist.\n')
        self.table.append(album)({'ID': int(ID), 'Title': album, 'Artist': artist})    

    def remove_album(self, ID):
        remove = input(str('Input the ID of the album you want to delete.\n'))
        CDRemoved = False
        count = 0
        for row in self:
            if row['ID'] == remove:   
                del self[count]
                CDRemoved = True
                break
            else:
                count += 1
        return CDRemoved
    
    def print_inventory(self):
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in self.table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
        
class UI():
    def print_menu():
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
        
    def menu_choice():
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]:\n').lower().strip()
        return choice


#------------- Script Start -------------#
invlist = CDInventory()
CDInventory.read_file(invlist)

while True:
    UI.print_menu()
    strChoice = UI.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled.\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            CDInventory.read_file(invlist)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        CDInventory.print_inventory(lstTbl)
        continue  # start loop back at top.
    elif strChoice == 'a':
        choice = ' '
        while choice not in ['y', 'n']:
            choice = input('Do you want to automatically assign an ID to this CD? [y/n]\n').strip().lower()
        invlist.input_album(choice)
        continue  # start loop back at top.
    elif strChoice == 'i':
        CDInventory.print_inventory(lstTbl)
        continue  # start loop back at top.
    elif strChoice == 'd':
        CDInventory.print_inventory(lstTbl)
        CDRemoved = CDInventory.remove_album(int(input('Which ID would you like to delete? ').strip()))
        if CDRemoved == True:
            print('The CD was removed.')
        else:
            print('Could not find this CD!')
        CDInventory.print_inventory(lstTbl)
        continue  # start loop back at top.
    elif strChoice == 's':
        CDInventory.print_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            CDInventory.write_file(strFileName, lstTbl)
            input('The inventory was successfully saved to file. Press [ENTER] to return to the menu.')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')