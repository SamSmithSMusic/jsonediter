#TODO BUILD THE MAKE OBJ LIST FUNCTION 

import json
import os

choice = 0
running = True
objects = []
attributeNum = 0
Concerts = []
Choirs = []
Years = []



def checkJson(prePath) :
    parts = prePath.split('.')
    if (((parts[-1].strip()).lower()) == 'json') :
        return True
    else : return False

def checkInt(lowbound,highbound,inbound):
    while (True):
        try:
            inboundInt = int(inbound)
            if inboundInt >= lowbound and inboundInt <= highbound :
                return inboundInt
            else :
                raise ValueError
        except ValueError:
            inbound = input('Invalid Entry, please try again : \n') 

def manageObjects(filePath):
    with open(filePath, 'r') as file:
        objects = json.load(file)

    os.system('cls')
    print('Objects Successfully loaded - \n')
    
    while (True):
        choice = checkInt(0,4,input("What would you like to do?\n1 : View all Objects with Attributes\n2 : Edit an Object\n3 : Append an Object\n4 : Remove an Object \n0 : Back to Main Menu"))
        if choice == 0:
            break
        elif choice == 1:
            viewObjects(objects)
        elif choice == 2:
            establishAttributes(objects)
            editObject(objects)
        elif choice == 3:
            appendObject(objects)
        elif choice == 4:
            removeObj(objects)

def establishAttributes(objects):
    #Can Be enhanced by setting concert attr's to what the user wants to make it universal.
    for attr in objects[0]:

        if attr == 'Concert':
            for obj in objects:
                if (obj[attr] not in Concerts):
                    Concerts.append(obj[attr])

        if attr == 'Choir':
            for obj in objects:
                if (obj[attr] not in Choirs):
                    Choirs.append(obj[attr])

        if attr == 'Year':
            for obj in objects:
                if (obj[attr] not in Years):
                    Years.append(obj[attr])

def viewObjects(objects):
    os.system('cls')
    print('Here is a list of the loaded objects and their attributes.')
    i = 0
    attributeNum = len(objects[1])

    for obj in objects:
        print(f'\n{i}')
        for key in objects[i]:
            print(f'    {key} : {obj[key]}')

        i+= 1
    
    print('\n')

def editObject(objects):
    viewObjects(objects)
    tempChoice = input('Please enter the number object you would like to change, Enter "quit" to return : ')
    if tempChoice.lower() == 'quit':
        return
    else:
        choice = checkInt(0,objects.length() -1, tempChoice)
    
    print(f"You've chosen to select the object at the index {choice}.")
    # Find which attribute with they'd want to change and iterate and change with set lists.

def appendObject(objects):
    pass

    

def manageAttributes(filePath):
    pass

def viewRaw(filePath):
    pass

def saveAs():
    pass
    






while running :
    inMenu = True
    loading = True

    os.system('cls')
    print('Welcome to my JSON editor!')

    while loading:
        # jsonPath = r"{}".format(input("Please input the absolute path to your json file:\n"))
        jsonPath = r'C:\Users\samsm\Downloads\performances.json'
        check = checkJson(jsonPath)
        

        if check :
            print(f"JSON file at {jsonPath} succesfully found.")
            break
        else:
            print(f"Invalid File Type at {jsonPath}, please try again.")

    
    while (inMenu):
        os.system('cls')
        choice = checkInt(0,3,input("What would you like to do with this json file?\n1 : Manage Objects\n2 : Manage Set Attributes\n3 : View Raw Json\n4 : SaveAs & Quit \n0 : Quit Without Saving"))
        if choice == 0:
            running = False
            break
        elif choice == 1:
            manageObjects(jsonPath)
        elif choice == 2:
            manageAttributes(jsonPath)
        elif choice == 3:
            viewRaw(jsonPath)
        elif choice == 4:
            saveAs(jsonPath)
        







    