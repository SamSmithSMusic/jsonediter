#TODO BUILD THE MANAGE ATTRIBUTES

import json
import os
import time
from datetime import datetime

choice = 0
running = True
objects = []
attributeNum = 0
#Concerts, Choirs, and Years are only referenced through the SetAttributes list further down.
Concerts = []
Choirs = []
Years = []
Attributes = []
SetAttributes = [Concerts,Choirs,Years]
SetAttrNames = ['Concerts','Choirs','Years']


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

def manageObjects():
    # with open(filePath, 'r') as file:
    #     objects = json.load(file)
    

    os.system('cls')
    print('Objects Successfully loaded - \n')
    
    while (True):
        establishAttributes(objects)
        choice = checkInt(0,4,input("\nWhat would you like to do?\n1 : View all Objects with Attributes\n2 : Edit an Object\n3 : Append an Object\n4 : Remove an Object \n0 : Back to Main Menu\n"))
        if choice == 0:
            break
        elif choice == 1:
            viewObjects()
        elif choice == 2:
            editObject()
        elif choice == 3:
            appendObject()
        elif choice == 4:
            removeObj()

def establishAttributes(objects):
    #Can Be enhanced by setting concert attr's to what the user wants to make it universal.
    for attr in objects[0]:

        if attr == 'Concert':
            for obj in objects:
                if (obj[attr] not in SetAttributes[0]):
                    SetAttributes[0].append(obj[attr])

        elif attr == 'Choir':
            for obj in objects:
                if (obj[attr] not in SetAttributes[1]):
                    SetAttributes[1].append(obj[attr])

        elif attr == 'Year':
            for obj in objects:
                if (obj[attr] not in SetAttributes[2]):
                    SetAttributes[2].append(obj[attr])

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

def viewObjects():
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

def editObject():
    viewObjects()
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

def appendObject():
    while True:

        i=0
        print('')
        for choir in SetAttributes[0]:
            print(f'{i} - {choir}')
            i+= 1
        newConcert = SetAttributes[0][checkInt(0,len(SetAttributes[0])-1,input('Please input the number associated with the Concert value you want : '))]

        i=0
        print('')
        for choir in SetAttributes[1]:
            print(f'{i} - {choir}')
            i+= 1
        newChoir = SetAttributes[1][checkInt(0,len(SetAttributes[1])-1,input('Please input the number associated with the Choir value you want : '))]

        newSong = input('Please enter the name of the song : ')
        newCredit = input('Please enter the credit for this song : ')

        i=0
        print('')
        for choir in SetAttributes[2]:
            print(f'{i} - {choir}')
            i+= 1
        newYear = SetAttributes[2][checkInt(0,len(SetAttributes[2])-1,input('Please input the number associated with the Year value you want : '))]     

        newSource = input('Please enter the link to the video from google drive of this performance : ')

        print(f'''
{Attributes[0]} - {newConcert}
{Attributes[1]} - {newChoir}
{Attributes[2]} - {newSong}
{Attributes[3]} - {newCredit}
{Attributes[4]} - {newYear}
{Attributes[5]} - {newSource}

Does this information look correct? (y/n) : 
''')
        yn = input()
        if yn.lower() == 'y':
            newObject = {
            Attributes[0] : newConcert,
            Attributes[1] : newChoir,
            Attributes[2] : newSong,
            Attributes[3] : newCredit,
            Attributes[4] : newYear,
            Attributes[5] : newSource}


            objects.append(newObject)
            print('Object Successfully added.')
            time.sleep(1)
            break
        else:
            print("Okay. let's try again - ")

def removeObj():
    while True:
        viewObjects()
        preremoveChoice = input('Please enter the number associated with the onject you would like to remove, enter "quit" to return to previous menu. : ')
        if preremoveChoice.lower() == 'quit':
            break
        removeChoice = checkInt(0,len(objects) -1,preremoveChoice)
        
        yn = input(f'Are you sure you want to remove - \n{objects[removeChoice]}\nfrom the json file? (y/n) : ')
        if yn.lower() == 'y':
            objects.pop(removeChoice)
            print('The object has been successfully removed.')
            time.sleep(1)
            break
        else :
            print()

def manageAttributes():
        os.system('cls')
        print('Attributes Successfully loaded - \n')
    
        while (True):
            establishAttributes(objects)
            choice = checkInt(0,3,input("\nWhat would you like to do?\n1 : View all Set Attributes\n2 : Add a Set Attribute option\n3 : Remove a Set Attribute option\n0 : Back to Main Menu\n"))
            if choice == 0:
                break
            elif choice == 1:
                viewSetAttr()
            elif choice == 2:
                addAttr()
            elif choice == 3:
                removeAttr()

def viewSetAttr():
    print('Here is a list of all set available attributes.')
    i =0
    for attr in SetAttributes:
        print(f'{i} : {SetAttrNames[i]}')
        k = 0
        for option in attr:
            print(f'      - {option}')
            k +=1
        i+= 1
        print()

def addAttr():
    viewSetAttr()
    prechoice = input('Please enter the number of the attribute you would like to add an option to (Enter "quit" to return): ')
    if prechoice.lower() == 'quit':
        return
    choice = checkInt(0,len(SetAttributes),prechoice)
    while True:
        newOption = input(f'Please enter the value you would like to add to {SetAttrNames[choice]} : ')
        yn = input(f'Are you sure you want to add {newOption} to the options for {SetAttrNames[choice]}? (y/n) : ')
        if yn.lower() == 'y':
            SetAttributes[choice].append(newOption)
            print('Option successfully added.')
            time.sleep(1)
            return
        print('Returning...')
        

def removeAttr():
    viewSetAttr()
    prechoice = input('Please enter the number of the attribute you would like to remove an option from (Enter "quit" to return): ')
    if prechoice.lower() == 'quit':
        return
    choice = checkInt(0,len(SetAttributes),prechoice)
    while True:
        i=0
        for value in SetAttributes[choice]:
            print(f'{i} - {value}')
            i+= 1
        newOption = checkInt(0,len(SetAttributes[choice]),input(f'Please enter the number of the Value you would like to remove from {SetAttrNames[choice]} : '))
        yn = input(f'Are you sure you want to remove {SetAttributes[choice][newOption]} from the options for {SetAttrNames[choice]}? (y/n) : ')
        if yn.lower() == 'y':
            SetAttributes[choice].pop(newOption)
            print('Option successfully removed.')
            time.sleep(1)
            return
        print('Returning...')

def saveAs():
    filePath = input('Please input the abosolute path to the directory you would like to save this file to.')
#    filePath = r'C:\Users\samsm\Desktop'
    yn = input('Would you like to name the file? (y/n) : ')
    fileName = datetime.now().strftime("%H-%M-%S")
    if yn.lower() == 'y':
        fileName = input('Enter the name : ')
    
    try:
        with open(filePath + f'\\{fileName}.json', 'w') as file:
            json.dump(objects,file, indent=4)
    except Exception as e:
        print(f'An Error occurred while saving: {e}\n\n Press ENTER to continue.')
        input()
    






while running :
    inMenu = True
    loading = True

    os.system('cls')
    print('Welcome to my JSON editor!')

    while loading:
        jsonPath = r"{}".format(input("Please input the absolute path to your json file:\n"))
        #jsonPath = r'C:\Users\samsm\Downloads\performances.json'
        check = checkJson(jsonPath)
        

        if check :
            with open(jsonPath, 'r') as file:
                objects = json.load(file)
            establishAttributes(objects)

            print(f"JSON file at {jsonPath} succesfully found.")
            break
        else:
            print(f"Invalid File Type at {jsonPath}, please try again.")

    
    while (inMenu):
        os.system('cls')
        choice = checkInt(0,3,input("What would you like to do with this json file?\n1 : Manage Objects\n2 : Manage Set Attributes\n3 : SaveAs \n0 : Quit Without Saving\n"))
        if choice == 0:
            running = False
            break
        elif choice == 1:
            manageObjects()
        elif choice == 2:
            manageAttributes()
        elif choice == 3:
            saveAs()
        







    