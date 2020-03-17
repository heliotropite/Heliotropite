#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AdamH, 2020-Feb-28, Added Functionality and organized script
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file objec

# -- PROCESSING -- #
class DataProcessor:
    """Processing the data in memory"""
    
    @staticmethod
    def add_album(lstInput):
        """Function to add a user-inputted line item to 2D data structure in memory

        Adds a dict to a 2D data structure (list of dicts) after processing user input.
        
        Args:
            lstInput (list): three item list inputted by the user to but inputted as [0]: ID, [1]: Album, and [2]: Artist.

        Returns:
            blnCDRemoved: True if a line was removed from the table, False if nothing was removed.
        """
        dicRow = {'ID': int(lstInput[0]), 'Title': lstInput[1], 'Artist': lstInput[2]}
        lstTbl.append(dicRow)
        
    @staticmethod    
    def delete_album(intIDDel):
        """Function to remove a specified item from a 2D data structure in memory

        Searches for and removes a dict from the list of dicts stored in memory, with the user inputting which
        item to search for.
        
        Args:
            intIDDel (int): Int inputted by the user, to iterate over the list searching for in the 'ID' value. 

        Returns:
            blnCDRemoved: True if a line was removed from the table, False if nothing was removed.
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        return(blnCDRemoved)

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(file_name, table):
        """Function to manage data writing into a text file

        Writes the data stored in the 2D data construct (list of dicts) into the text file specified by strFileName.
        Turns the list of dicts into a .csv format before writing to file.
        
        Args:
            file_name (string): name of file used to write the data to
            table (list of dict): 2D data structure (list of dicts) that held the data during runtime

        Returns:
            None.
        """        
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def input_album():
        """Function to allow the user to input a new inventory item to be inputted later into our 2D data stucture in memory

        Prompts the user to enter an ID, Album, and Artist as strings.
        
        Args:
            None.

        Returns:
            StrID, strTitle, strArtist: Three outputs, each a string, inputted by the user to be used by other functions. 
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist

FileProcessor.read_file(strFileName, lstTbl)

while True:
    IO.print_menu()
    strChoice = IO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled.\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    elif strChoice == 'a':
        DataProcessor.add_album(IO.input_album())
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.show_inventory(lstTbl)
        blnCDRemoved = DataProcessor.delete_album(int(input('Which ID would you like to delete? ').strip()))
        if blnCDRemoved:
            print('The CD was removed.')
        else:
            print('Could not find this CD!')
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    elif strChoice == 's':
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileProcessor.write_file(strFileName, lstTbl)
            input('The inventory was successfully saved to file. Press [ENTER] to return to the menu.')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')