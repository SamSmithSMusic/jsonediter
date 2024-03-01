#TODO BUILD THE MAKE OBJ LIST FUNCTION 

import json
import os


def makeObjList(rawJson):
    pass

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
            print('Invalid Entry, please try again : \n') 

def manageObjects(filePath):
    with open(filePath, 'r') as file:
        objects = makeObjList(json.load(file))

    os.system('cls')
    print('Objects Successfully loaded - \n')
    
    while (True):
        choice = checkInt(0,3,input("What would you like to do?\n1 : View all Objects with Attributes\n2 : Edit an Object\n3 : Append an Object\n4 : Remove an Object \n0 : Back to Main Menu"))
        if choice == 0:
            break
        elif choice == 1:
            viewObjects(objects)
        elif choice == 2:
            editObject(objects)
        elif choice == 3:
            appendObject(objects)
        elif choice == 4:
            saveAs(objects)

def viewObjects(objects):
    os.system('cls')
    print('Here is a list of the loaded objects and their attributes.')
    i = 0
    for obj in objects:
        i+= 1
        print(f'{i} - {obj}\n')
        print('\n\n\n')

def editObject(objects):
    pass

def appendObject(objects):
    pass

    

def manageAttributes(filePath):
    pass

def viewRaw(filePath):
    pass

def saveAs():
    pass
    




choice = 0
running = True

while running :
    inMenu = True
    loading = True

    os.system('cls')
    print('Welcome to my JSON editor!')

    while loading:
        jsonPath = r"{}".format(input("Please input the absolute path to your json file:\n"))
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
        







    