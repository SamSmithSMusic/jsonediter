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
Attributes = []



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
    establishAttributes(objects)

    os.system('cls')
    print('Objects Successfully loaded - \n')
    
    while (True):
        os.system('cls')
        choice = checkInt(0,4,input("What would you like to do?\n1 : View all Objects with Attributes\n2 : Edit an Object\n3 : Append an Object\n4 : Remove an Object \n0 : Back to Main Menu\n"))
        if choice == 0:
            break
        elif choice == 1:
            viewObjects(objects)
        elif choice == 2:
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

        elif attr == 'Choir':
            for obj in objects:
                if (obj[attr] not in Choirs):
                    Choirs.append(obj[attr])

        elif attr == 'Year':
            for obj in objects:
                if (obj[attr] not in Years):
                    Years.append(obj[attr])

        if attr not in Attributes:
            Attributes.append(attr)

def checkAttr(preattr):
    wrong = True
    while (wrong):
        attr = preattr.lower().capitalize()
        if  attr in Attributes:
            wrong = False
            return attr
        else : preattr = input('Inncorect Attribute, please try again : ')

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
        choice = checkInt(0,len(objects) -1, tempChoice)
    
    print(f"\nYou've chosen to edit the object at the index {choice}.")
    
    i = 0
    for key in objects[choice]:
        print(f'{key} : {objects[choice][key]}' )
    tempattrChoice = input('\nWhich attribute of this class would you like to change? Enter "Quit" to return to previous menu. : ')
    if tempattrChoice.lower() == 'quit':
        return
    attrChoice = checkAttr(tempattrChoice)

    if attrChoice.lower() == 'concert':

        while (True):
            print(f'The current value of Concert is {objects[choice]["Concert"]}\n')
            i =0
            for concert in Concerts:
                print(f'{i} - {concert}')
                i+= 1
            newchoice = checkInt(0,len(Concerts) -1,input('Please enter the number of the value you would like to change to : '))
            yn = input(f'You are about to change the value {objects[choice]["Concert"]}, to {Concerts[newchoice]}. Confirm? (y/n) : ')
            if yn.lower() == 'y':
                objects[choice]['Concert'] = Concerts[newchoice]
                break

    elif attrChoice.lower() == 'choir':

        while (True):
            print(f'The current value of Choir is {objects[choice]["Choir"]}\n')
            i =0
            for choir in Choirs:
                print(f'{i} - {choir}')
                i+= 1
            newchoice = checkInt(0,len(Choirs) -1,input('Please enter the number of the value you would like to change to : '))
            yn = input(f'You are about to change the value {objects[choice]["Choir"]}, to {Choirs[newchoice]}. Confirm? (y/n) : ')
            if yn.lower() == 'y':
                objects[choice]['Choir'] = Choirs[newchoice]
                break

    elif attrChoice.lower() == 'year':

        while (True):
            print(f'The current value of Year is {objects[choice]["Year"]}\n')
            i =0
            for year in Years:
                print(f'{i} - {year}')
                i+= 1
            newchoice = checkInt(0,len(Years) -1,input('Please enter the number of the value you would like to change to : '))
            yn = input(f'You are about to change the value {objects[choice]["Year"]}, to {Years[newchoice]}. Confirm? (y/n) : ')
            if yn.lower() == 'y':
                objects[choice]['Year'] = Years[newchoice]
                break

    else:
        while (True):
            newValue = input(f'The current value of {attrChoice} is {objects[choice][attrChoice]}\nWhat would you like to change it to? : ')
            yn = input(f'You are about to change the value {objects[choice][attrChoice]}, to {newValue}. Confirm? (y/n) : ')
            if yn.lower() == 'y':
                objects[choice][attrChoice] = newValue
                break

def appendObject(objects):
    pass

def removeObject(objects):
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
        choice = checkInt(0,3,input("What would you like to do with this json file?\n1 : Manage Objects\n2 : Manage Set Attributes\n3 : View Raw Json\n4 : SaveAs & Quit \n0 : Quit Without Saving\n"))
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
        







    